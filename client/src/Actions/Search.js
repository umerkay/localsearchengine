export const SearchReq = (dispatch, searchValue, page, pageSize = 11) => {
    if(!searchValue || (!page && page !== 0)) return
    dispatch({
        type: "SEARCH_DOCS_REQUEST"
    });

    fetch(`/search?q=${searchValue.trim()}&pageStart=${page - 1}&pageSize=${pageSize}`)
        .then(response => response.json())
        .then(jsonResponse => {
            console.log(jsonResponse)
        if (jsonResponse.Response === true) {
            dispatch({
            type: "SEARCH_DOCS_SUCCESS",
            payload: { docs: jsonResponse.Search, searchValue, totalResults: jsonResponse.totalResults, time: jsonResponse.time }
            });
        } else {
            dispatch({
            type: "SEARCH_DOCS_FAILURE",
            error: jsonResponse.Error
            });
        }
        });
};