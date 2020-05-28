import React, {Component} from "react";
import styled from 'styled-components';
import {buildLogoutLink} from "../utils/Auth";
import {eraseCookie} from "../utils/Cookies";

const LogoutButton = styled.button`
    margin:5px;
    width: 165px;
    height:35px;
    border-radius: 4px;
    background: #EC7063;
    color:white;
    border:0px transparent;
    text-align: center;

    &:hover{
        background: #3b5998;
        opacity: 0.6;
    }
`;

class Logout extends Component{

    handleClick(){
        eraseCookie('accessToken');
        window.location.href = buildLogoutLink();
        return null;
    }

    render(){
      return (
         <div className="login-button"
              onClick={this.handleClick}>
              <LogoutButton className="text">Logout</LogoutButton>
         </div>);
    }
}

export default Logout;