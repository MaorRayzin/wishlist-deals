import {applyMiddleware, createStore} from 'redux'
import reducers from './reducers/combinedReducers';

import promiseMiddleware from 'redux-promise-middleware'
import thunkMiddleware from 'redux-thunk'
import loggerMiddleware from 'redux-logger'

const middleware = applyMiddleware(promiseMiddleware(), thunkMiddleware, loggerMiddleware);
export default createStore(reducers, middleware);