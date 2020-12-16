import React from "react";
import {MDBContainer, MDBBtn, Grid, FormRow} from "mdbreact";
import './NotFound.css'


export const NotFound = () => (
    <MDBContainer>
        <Grid container spacing={1}>
            <Grid container item xs={12} spacing={3}>
                <FormRow/>
            </Grid>
            <Grid container item xs={12} spacing={3}>
                <FormRow/>
            </Grid>
            <Grid container item xs={12} spacing={3}>
                <FormRow/>
            </Grid>
        </Grid>
    </MDBContainer>
);