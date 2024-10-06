import React, { useState, useEffect } from 'react';
import { Page, Navbar, NavLeft, NavTitle, Link, Progressbar } from 'framework7-react';
import { CosmographProvider, Cosmograph, CosmographTimeline } from '@cosmograph/react';

const BaseURL = 'http://0.0.0.0';

const HomePage = () => {
  const [loading, setLoading] = useState(false);
  const [nodes, setNodes] = useState([]);
  const [links, setLinks] = useState([]);
  const colors = ['#88C6FF', '#FF99D2', '#2748A4'];

  useEffect(() => {
    setLoading(true);
    fetch(`${BaseURL}/screenshots`)
      .then(response => response.json())
      .then(data => {
        const newNodes = new Set();
        const newLinks = [];

        data.forEach(screen => {
          screen.graph.forEach(graphItem => {
            // Ensuring unique nodes
            newNodes.add(graphItem.source);
            newNodes.add(graphItem.target);

            // Create links with datetime as an additional property
            newLinks.push({
              source: graphItem.source,
              target: graphItem.target,
              date: new Date(screen.datetime),
              relationship: graphItem.relationship_name
            });
          });
        });

        // Converting Set back to array for React state
        setNodes(Array.from(newNodes).map(node => ({ id: node })));
        setLinks(newLinks);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setLoading(false);
      });
  }, []);

  return (
      <Page name="home">
        <Navbar sliding={false}>
          <NavLeft>
            <Link iconIos="f7:menu" iconMd="material:menu" panelOpen="left" />
          </NavLeft>
          <NavTitle sliding>Mistral Etoile</NavTitle>
        </Navbar>

        {loading && <Progressbar infinite color="multi" />}
        <div style={{ height: '500px', width: '100%' }}>
            <CosmographProvider nodes={nodes} links={links}>
              <Cosmograph
                nodeSize={5}
                nodeColor={() => colors[Math.floor(Math.random() * colors.length)]}
                linkWidth={() => 1 + 2 * Math.random()}
                linkColor={() => colors[Math.floor(Math.random() * colors.length)]}
               />
              <CosmographTimeline showAnimationControls />
            </CosmographProvider>
        </div>
      </Page>
  );
};

export default HomePage;
