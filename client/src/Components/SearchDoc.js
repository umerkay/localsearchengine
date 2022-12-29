import React from 'react';
import { Link } from 'react-router-dom';

const baseUrl = "" //process.env.PUBLIC_URL;
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faStar, faGlobe, faClock } from '@fortawesome/free-solid-svg-icons'

export default function SearchDoc({ doc, relevance, isDummy = false }) {
  return (
    <>
      {
        isDummy ? (
          <a className='searchDoc dummy'>
            <div className="title"></div>
            <div className='about'></div>
          </a>
        ) : (<>{
          relevance ? (
            <a className='searchDoc relevant' href={doc.url}>
              <div className='imp'>
                <FontAwesomeIcon icon={faStar}></FontAwesomeIcon>
                <span>High Relevance</span>
              </div>
              <div className="title">{doc.Title.split("--")[2]}</div>
              <div className='about'>
              <FontAwesomeIcon icon={faGlobe}></FontAwesomeIcon>
              <span>{doc.Title.split("--")[0]}</span>
              <FontAwesomeIcon icon={faClock}></FontAwesomeIcon>
              <span>{doc.Title.split("--")[1]}</span>
              {/* <span>{doc.Score}</span> */}
              </div></a>
          ) : (
            <a className='searchDoc' href={doc.url}>
              <div className="title">{doc.Title.split("--")[2]}</div>
              <div className='about'>
              <FontAwesomeIcon icon={faGlobe}></FontAwesomeIcon>
              <span>{doc.Title.split("--")[0]}</span>
              <FontAwesomeIcon icon={faClock}></FontAwesomeIcon>
              <span>{doc.Title.split("--")[1]}</span>
              {/* <span>{doc.Score}</span> */}
              </div></a>
          )
          }</>)
      }
    </>
  );
}