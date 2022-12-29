import React, { useState } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faInfo, faSpinner, faTruckLoading, faUpload } from '@fortawesome/free-solid-svg-icons'

function FileUploadForm() {
    const [message, setMessage] = useState(null)
    const [isLoading, setIsLoading] = useState(false)
  const handleSubmit = (event) => {
    event.preventDefault();

    const formData = new FormData();
    const files = event.target.elements.files.files;

    for (let i = 0; i < files.length; i++) {
      formData.append("files", files[i]);
    }

    setIsLoading(true);
    fetch("/upload", {
      method: "POST",
      body: formData,
    }).then(res => res.json()).then(json => {
        setMessage(json.msg);
        setIsLoading(false);
    });
  };

  return (
    isLoading ?
        (<>{"Indexing.."} <FontAwesomeIcon icon={faSpinner}></FontAwesomeIcon></>):
        (
    <form onSubmit={handleSubmit}>
      <input type="file" name="files" accept=".json" multiple />
      <button className="btn" type="submit">   

      Upload <FontAwesomeIcon icon={faUpload}></FontAwesomeIcon>
        
      </button>
      <span style={{width: "100%", textAlign: "center"}}>
      {message ?
        (<>{message} <FontAwesomeIcon icon={faInfo}></FontAwesomeIcon></>):
        (null)}
        </span>
    </form>)
  );
}

export default FileUploadForm;
