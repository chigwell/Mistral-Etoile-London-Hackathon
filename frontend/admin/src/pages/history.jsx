import React, { useState, useEffect, useRef } from 'react';
import { Page, BlockTitle, Navbar, PhotoBrowser, Progressbar, List, ListItem } from 'framework7-react';
import { format, parseISO } from 'date-fns';  // Import necessary functions from date-fns

const BaseURL = 'http://0.0.0.0';

const HistoryPage = () => {
  const [loading, setLoading] = useState(false);
  const [images, setImages] = useState([]);
  const photoBrowserRef = useRef(null);
  const intervalRef = useRef(null);

  useEffect(() => {
    loadImages();

    intervalRef.current = setInterval(() => {
      console.log('Checking for new images...');
      loadImages();
    }, 30000);

    return () => clearInterval(intervalRef.current);
  }, []);

  const loadImages = () => {
    setLoading(true);
    fetch(`${BaseURL}/screenshots`)
      .then(response => response.json())
      .then(data => {
        const imageObjects = data.map(image => ({
          ...image,
          filename: `Screenshot ID ${image.id}`,
          formattedDatetime: format(parseISO(image.datetime), 'PPPppp'),
          isLoading: true  // Add isLoading state
        }));
        setImages(imageObjects);  // Update state immediately with placeholder data
        fetchDescriptions(imageObjects);
      })
      .catch(error => {
        console.error('Error fetching images:', error);
        setLoading(false);
      });
  };

  const fetchDescriptions = (imageObjects) => {
    const updatedImages = imageObjects.map(image => ({ ...image }));  // Clone to trigger re-render

    imageObjects.forEach((image, index) => {
      if (!image.description) {
        fetch(`${BaseURL}/description?id=${image.id}`)
          .then(response => response.json())
          .then(data => {
            updatedImages[index].description = data.description;
            updatedImages[index].isLoading = false;  // Update isLoading state
            setImages([...updatedImages]);
          })
          .catch(error => {
            console.error(`Error fetching description for ID ${image.id}:`, error);
            updatedImages[index].description = "Error fetching description";
            updatedImages[index].isLoading = false;
            setImages([...updatedImages]);
          });
      } else {
        updatedImages[index].isLoading = false;
        setImages([...updatedImages]);
      }
    });
  };

  return (
    <Page>
      <Navbar title="History (only for debug)" backLink="Back" />
      {loading && <Progressbar infinite color="multi" />}
      <PhotoBrowser
        photos={images.map(image => ({
          url: image.link,
          caption: image.caption || "",
          description: image.description || "Loading description...",
        }))}
        theme="light"
        type="standalone"
        ref={photoBrowserRef}
      />
      <BlockTitle>Image Timeline</BlockTitle>
      <List mediaList>
        {images.map((image, index) => (
          <ListItem
            style={{ whiteSpace: "break-spaces" }}
            key={image.filename}
            link="#"
            title={image.formattedDatetime || "No date provided"}
            subtitle={image.description || "Loading description..."}
            text={image.caption || ""}
            onClick={() => photoBrowserRef.current.open(index)}
          >
            <img slot="media" style={{ borderRadius: '8px' }} src={image.isLoading ? 'path/to/placeholder.png' : image.link} width="80" />
          </ListItem>
        ))}
      </List>
    </Page>
  );
};

export default HistoryPage;
