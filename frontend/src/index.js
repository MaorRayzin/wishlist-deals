import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';


import './index.css';

import mystore from './store';
import App from './components/App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<Provider store={mystore}><App/></Provider>, document.getElementById('root'));
registerServiceWorker();
