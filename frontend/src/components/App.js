import React, { Component } from "react";
import { render } from "react-dom";

export default class App extends Component {
    // we don't have to know what this means, Just initial setup
    constructor(props) {
        super(props);
    }
    render() {
        return (

        <h1>Testing React Code</h1>

        );
    }
}
const appDiv = document.getElementById("app"); // to make access inside the app container in index.html file 
render(<App/>, appDiv); // -> then put it into index.js