import React, { Component } from "react";
import CreateRoomPage from "./CreateRoomPage";
import JoinRoomPage from "./JoinRoomPage";
import {
    BrowserRouter as BRouter,
    Routes,//instead of Switch after react-router-dom v6
    Route,
    Link,
    Redirect,

} from "react-router-dom";

export default class HomePage extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <BRouter>
                <Routes>
                    <Route exact path="/" element={<p>This is a Home page </p>}></Route>
                    <Route  path="/join" element={<JoinRoomPage/>}></Route>
                    <Route path="/create" element={<CreateRoomPage/>}/>
                </Routes>
            </BRouter>
        );
    }
}