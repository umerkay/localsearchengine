import React, { useEffect, useState } from 'react';
import LoadingGif from './loading.gif';
import SearchDoc from './SearchDoc';

export default function DocsContainer({ setPage, page, loading, errorMessage, docs, search, match, time, totalResults }) {

  const pageSize = 11

  useEffect(() => {
    search(match.params.q, page, pageSize)
    // setPage(0)
  }, [page, pageSize]);

  return (
    <div className="docsContainer">
      {
        loading ? (<>
          <span>
            Looking for documents...
          </span>
          <div className="docs">
            {Array(12).fill().map((x,i) => (
              <SearchDoc key={i} isDummy={true}/>
            ))}
          </div></>
        ) : (<>
          <span>
            {totalResults > 0 ? (<>I found {totalResults} documents in {time}</>) : (<>Unfortunately, I could not find any documents. Try making your query more specific or use a word that may be more common.</>)}
            
          </span>
          <div className="docs">
            {docs.map((doc, index) => (
              <SearchDoc key={index} doc={doc} relevance={page === 1 && index < 3}/>
            ))}
          </div></>
        )
      }
      
      <div className="info">
        {errorMessage ? (
          <div className="errorMessage">Sorry, the search could not be made because the server returned an error: {errorMessage}</div>
        ) : null
        }
      </div>

      <div className="info">
        {totalResults > 0 ? (
          <div className="pagenation">Page
          <input type="number" value={page} min={1} onInput={e => setPage(e.target.value)} />
          of {Math.ceil(totalResults / 11)}</div>
        ) : null
        }
      </div>
    </div>
  )
}
