import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { createRoot } from 'react-dom/client';

const root = createRoot(document.getElementById('root')); // createRoot(container!) if you use TypeScript
root.render(<App tab="home" />);