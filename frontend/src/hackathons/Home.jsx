import React, {Component} from 'react';
import Logout from "../login/Logout";
import HackathonList from "./HackathonList";

class Home extends Component {
    render() {
        return (
            <div className="home">
                <Logout/>
                <HackathonList/>
            </div>
        );
    }
}

export default Home;
