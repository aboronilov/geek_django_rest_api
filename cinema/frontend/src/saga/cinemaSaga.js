import {call, put, takeEvery} from 'redux-saga/effects'
import { FETCH_CINEMAS, setCinemas } from '../store/cinemaReducer'

const fetchCinemasFromApi = () => fetch('http://127.0.0.1:8000/api/cinema/')
console.log(fetchCinemasFromApi)

function* fetchCinemasWorker() {
    const data = yield call(fetchCinemasFromApi)
    const json = yield call(() => new Promise(res => res(data.json())))    
    yield put(setCinemas(json.results))
}

export function* cinemaWatcher() {
    yield takeEvery(FETCH_CINEMAS, fetchCinemasWorker)
}