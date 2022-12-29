import React, { useState } from "react";
import { Link, withRouter } from "react-router-dom";
import Modal from "./Modal";

const baseUrl = "" //process.env.PUBLIC_URL;
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch, faPlus } from '@fortawesome/free-solid-svg-icons'

const Search = (props) => {
  const [searchValue, setSearchValue] = useState(props.match.params.q || "");
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleSearchInputChanges = (e) => {
    setSearchValue(e.target.value);
  }

  const resetInputField = () => {
    setSearchValue("");
  }

  const callSearchFunction = (e) => {
    e.preventDefault();
    if (!searchValue) return;

    props.history.push(baseUrl + "/search/" + searchValue);
    // props.setPage(0)
    props.search(searchValue, props.page);
  }

  return (
    <>
    <form className="search" onSubmit={callSearchFunction}>
      <input
        value={searchValue}
        onChange={handleSearchInputChanges}
        type="text"
        placeholder="Search"
        disabled={isModalOpen}
      />
      <Link className="submitSearch" onClick={callSearchFunction} to={"/search/" + searchValue.trim()}>
        <FontAwesomeIcon icon={faSearch}></FontAwesomeIcon>
      </Link>
      <Link className="btn" onClick={() => setIsModalOpen(true)}>
        <FontAwesomeIcon icon={faPlus}></FontAwesomeIcon>
      </Link>
    </form>
      <Modal isOpen={isModalOpen} closeModal={() => setIsModalOpen(false)} />
    </>
  );
}

export default withRouter(Search);