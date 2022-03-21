import createSagaMiddleware from 'redux-saga'
import userReducer from './userReducer'
import cinemaReducer from './cinemaReducer'
import {applyMiddleware, combineReducers, createStore} from "redux";
import { rootWatcher } from '../saga';

const sagaMiddleware = createSagaMiddleware()

const rootReducer = combineReducers({
      userReducer,
      cinemaReducer,
})

export const store = createStore(rootReducer, applyMiddleware(sagaMiddleware))

sagaMiddleware.run(rootWatcher)