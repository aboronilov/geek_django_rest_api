import {call, put, takeEvery} from 'redux-saga/effects'
import { FETCH_USERS, setUsers } from '../store/userReducer'

const fetchUsersFromApi = () => fetch('http://127.0.0.1:8000/api/users/')

function* fetchUserWorker() {
    const data = yield call(fetchUsersFromApi)
    const json = yield call(() => new Promise(res => res(data.json())))    
    yield put(setUsers(json.results))
}

export function* userWatcher() {
    yield takeEvery(FETCH_USERS, fetchUserWorker)
}