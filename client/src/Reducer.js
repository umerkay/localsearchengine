export const initialState = {
  loading: false,
  docs: [],
  errorMessage: null,
  page: 0,
  time: null,
  searchValue: ""
};

export const reducer = (state, action) => {
  switch (action.type) {
    case "SEARCH_DOCS_REQUEST":
      return {
        ...state,
        loading: true,
        errorMessage: null,
        docs: []
      };
    case "LOAD_MORE_REQUEST":
      return {
        ...state,
        loading: true,
        errorMessage: null
      };
    case "SEARCH_DOCS_SUCCESS":
      return {
        ...state,
        loading: false,
        docs: action.payload.docs,
        page: action.payload.page,
        searchValue: action.payload.searchValue,
        totalResults: action.payload.totalResults,
        time: action.payload.time
      };
    case "LOAD_MORE_SUCCESS":
      return {
        ...state,
        loading: false,
        docs: action.payload.docs,
        page: action.payload.page
      };
    case "SEARCH_DOCS_FAILURE":
      return {
        ...state,
        loading: false,
        errorMessage: action.error,
        docs: [],
        page: null,
        searchValue: null
      };
    default:
      return state;
  }
};