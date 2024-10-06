# Mistral Etoile Project Suite

The `Etoile` project suite is a comprehensive collection of tools and services designed to leverage advanced machine learning and natural language processing technologies to analyze, generate, and visualize data across various domains. This suite includes several Python packages published on PyPI, a FastAPI server for real-time data processing, a browser extension for data capture, and a React-based front-end UI for data visualization and administration.

## Packages

The suite includes the following packages available on PyPI:
- [etoile_generate](https://pypi.org/project/etoile-generate/) - Core functionality for generating structured data from natural language.
- [etoile_graph](https://pypi.org/project/etoile-graph/) - Tools for constructing knowledge graphs from text.
- [etoile_pixtral_safety](https://pypi.org/project/etoile-pixtral-safety/) - Mechanisms for detecting harmful content in images.
- [etoile_pixtral_description](https://pypi.org/project/etoile-pixtral-description/) - Detailed description generation for enhancing content analysis and SEO.
- [etoile_insights](https://pypi.org/project/etoile-insights/) - Extraction of insights related to psychological traits, professional potentials, and personal interests.

## FastAPI Server

The FastAPI server serves as the backbone for real-time data processing and API management. It requires API keys from Mistral AI and ImgBB for full functionality.

### Setting API Keys
Set the API keys by exporting them into your environment:
```bash
export MISTRAL_API_KEY=<your_mistral_api_key_here>
export API_IMAGE_KEY=<your_imgbb_api_key_here>
```

### Running the Server
Start the FastAPI server using uvicorn with the following command:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 80
```

## Browser Extension

The browser extension is designed to capture screenshots and send them to the FastAPI server for processing. It supports Chrome and Brave browsers.

### Installation
1. Navigate to `chrome://extensions/` or `brave://extensions/`.
2. Enable "Developer mode" at the top right corner.
3. Click "Load unpacked" and select the folder `brave-chrome-extension`.
4. The extension will start sending captured images to `http://0.0.0.0/screenshot`.

## Front-End UI

The front-end UI provides a minimal viable product (MVP) interface for visualizing data processed by the FastAPI server.

### Running the Front-End
Navigate to the front-end directory and run:
```bash
npm run dev
```

This command starts the development server, allowing you to interact with the visualized data, including graphs, lists, and detailed insight reports.

## Usage and Examples

To utilize the functionality provided by the `Etoile` suite, refer to the individual package documentation linked above. Each package includes examples and detailed usage instructions tailored to its specific capabilities.

## Contributions and Feedback

Contributions, feedback, and issues are warmly welcomed.

## License

All components of the `Etoile` suite are licensed under the MIT License. 