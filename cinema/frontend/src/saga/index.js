import {all} from "redux-saga/effects"
import { cinemaWatcher } from "./cinemaSaga"
import { userWatcher } from "./userSaga"

export function* rootWatcher() {
    yield all([userWatcher(), cinemaWatcher()])
}