import React, {Component} from 'react';
import {
    CardWrapper,
    CardHeader,
    CardHeading,
    CardBody,
    CardFieldset,
    CardOptionsNote,
    CardButton
} from "./Card";
import './HackathonList.css';
import {getCookie} from "../utils/Cookies";

class HackathonList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            hackathons: []
        };
    }

    componentDidMount() {
        fetch("/hackathons", {
            method: 'get',
            headers: new Headers({
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + getCookie('accessToken')
            })
        })
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        hackathons: result.hackathons
                    });
                },
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error: error
                    });
                }
            )
    }

    render() {
        const {error, isLoaded, hackathons} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return (


                <div className="hackathon-list">
                    {hackathons.map(hackathon => (
                        <CardWrapper>
                            <CardHeader>
                                <CardHeading>{hackathon.name}</CardHeading>
                            </CardHeader>

                            <CardBody>
                                <CardFieldset>
                                    <CardOptionsNote>Where: {hackathon.place_name}</CardOptionsNote>
                                    <CardOptionsNote>Start time: {hackathon.start_time}</CardOptionsNote>
                                    <CardOptionsNote>End time time: {hackathon.end_time}</CardOptionsNote>
                                </CardFieldset>

                                <CardButton type="button">Interested</CardButton>

                            </CardBody>
                        </CardWrapper>
                    ))}
                </div>
            );
        }
    }
}

export default HackathonList;