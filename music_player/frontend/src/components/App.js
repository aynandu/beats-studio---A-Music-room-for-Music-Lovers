import React, { Component } from "react";
import { createRoot } from "react-dom/client"
import HomePage from "./HomePage";


export default class App extends Component{
    constructor(props){
        super(props);
    }
    render(){
        //return <h1>{this.props.name}</h1>;
        return <HomePage/>;   
    }
}

const appDiv = document.getElementById("app");
const root = createRoot(appDiv);
//root.render(<App name="Tyson" />);
root.render(<App/>);

