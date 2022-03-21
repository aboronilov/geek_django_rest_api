const defaultState = {
    cinemas: []
}

export const SET_CINEMAS = "SET_CINEMAS"
export const FETCH_CINEMAS = "FETCH_CINEMAS"

export default function cinemaReducer(state=defaultState, action) {
    switch (action.type) {
        case SET_CINEMAS:
            return {...state, cinemas: action.payload}
        default:
            return state
    }
}

export const setCinemas = payload => ({type: SET_CINEMAS, payload})
export const fetchCinemas = () => ({type: FETCH_CINEMAS})