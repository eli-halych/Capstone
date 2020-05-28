import React, {Component} from "react";
import styled from 'styled-components';
import { buildLoginLink } from '../utils/Auth';

const LoginButton = styled.button`
    margin:5px;
    width: 165px;
    height:35px;
    border-radius: 4px;
    background: #db3236;
    color:white;
    border:0px transparent;
    text-align: center;

    &:hover{
        background: #3b5998;
        opacity: 0.6;
    }
`;

class Login extends Component{

    handleClick(){
        window.location.href = buildLoginLink('hackathons');
        return null;
    }

    render(){
      return (
         <div className="login-button"
              onClick={this.handleClick}>
              <LoginButton className="text" href="">Login</LoginButton>
         </div>);
    }
}

export default Login;