import React from "react";
import { useSpring, animated } from "react-spring";
import FileUploadForm from "./FileUploadForm";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCheck } from '@fortawesome/free-solid-svg-icons'


function Modal({ isOpen, closeModal }) {
//   const style = useSpring({
//     transform: isOpen ? "translateY(0)" : "translateY(-20%)",
//   });

  return (
    isOpen ? (
        <animated.div className="modal" onClick={closeModal}>
            <div className="modalChild" onClick={(e) => e.stopPropagation()}>
            <div className="modal-body">
            <h1>Index Documents</h1>
            <FileUploadForm></FileUploadForm>
            <button style={{width: "100%"}} className="btn" onClick={closeModal}>Done
              <FontAwesomeIcon icon={faCheck}></FontAwesomeIcon>
            </button>
            </div>
            </div>
        </animated.div>) : null
  );
}

export default Modal;
