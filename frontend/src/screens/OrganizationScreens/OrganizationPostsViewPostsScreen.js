import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
// import Moment from 'react-moment';
import moment from "moment";

import { useDispatch, useSelector } from "react-redux";
import {
    Card,
    Container,
    Form,
    Button,
    Row,
    Col,
    Table,
    Modal,
    Alert,
    Navbar,
    Nav,
} from "react-bootstrap";
import Select from "react-select";

import axios from "axios";
import {
    organizationPostsWorkloadDataList,
    organizationPostslist,
    organizationsPostsUpdatePost,
} from "../../actions/organizationActions";



import { listMembers } from "../../actions/memberActions";
import Loader from "../../components/Loader";
import Message from "../../components/Message";

const benchMarkOptions = [
    { value: "DVD", label: "DVD " },
    { value: "NDBench", label: "NDBench" },
];

const workloadMetricOptions = [
    { value: "CPU", label: "CPU" },
    { value: "NetworkIn", label: "NetworkIn" },
    { value: "NewtworkOut", label: "NewtworkOut" },
    { value: "Memory", label: "Memory" },
];
const dataTypeOptions = [
    { value: "Training Data", label: "Training Data" },
    { value: "Testing Data", label: "Testing Data" },
];
let timestamp = Date.now();
timestamp = new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
}).format(timestamp);
console.log();


function OrganizationPostsViewPostsScreen({ organizationPostsWorkLoadData}) {
    //const organizationPost = []
    // const dateToFormat = '1976-04-19T12:59-0500';
    // const [editModel, setEditmodel] = useState(false);
    // const [selectedPost, setSelectedPost] = useState({});
// 
    // const [requirementInformation, setRequirementInformation] = useState("");
    // const [addressLocation, setAddressLocation] = useState("");
    // const [addressStreet, setAddressStreet] = useState("");
    // const [MemberSelected, setMemberSelected] = useState("");
    // const [post_id, setPost_id] = useState("");
    // const [post, setPost] = useState("");

    const [benchMark, setBenchMark] = useState("");
    const [workloadMetric, setWorkloadMetric] = useState("");
    const [dataType, setDataType] = useState("");
    const [batchUnit, setBatchUnit] = useState("");
    const [batchID, setBatchID] = useState("");
    const [batchSize, setBatchSize] = useState("");
   
  


    const dispatch = useDispatch();

    // const memberList = useSelector((state) => state.memberList);
    // const {
    //     error: errorMemberList,
    //     loading: loadingMembers,
    //     members,
    // } = memberList;

    
    const organizationPostsWorkloadDataList = useSelector(
        (state) => state.organizationPostsWorkloadDataList
    )
    const { organizationPostsWorkLoadDatas } = organizationPostsWorkloadDataList;



    // const organizationLogin = useSelector((state) => state.organizationLogin);
    // const { organizationInfo } = organizationLogin;

    // const organizationPostUpdateList = useSelector(
    //     (state) => state.organizationPostUpdateList
    // );
    // const {
    //     error: errorOrganizationPostUpdateList,
    //     loading: loadingOrganizationPostUpdateList,
    //     organizationPostsUpdatePost,
    // } = organizationPostUpdateList;

    // useEffect(() => {
    //     // if (!organizationInfo) {
    //     //     // history.push('/OrganizationLoginScreen')
    //     // } else {
    //     //     dispatch(listMembers());
    //     //     dispatch(organizationPostslist(organizationInfo._id));
    //     // }

    // }, [history, organizationPostsUpdatePost, errorOrganizationPostUpdateList]);

    // const editOrganizationPost = (data) => {
    //     console.log(data);

    //     setEditmodel(true);
    //     setSelectedPost(data);

    //     setRequirementInformation(data.requirementInformation);
    //     setAddressLocation(data.addressLocation);
    //     setMemberSelected(data.MemberSelected);
    //     setPost_id(data._id);

    //     console.log(members);
    // };
    // const handleClose = () => {
    //     setEditmodel(false);
    // };
    // const handleChange = (e) => {
    //     console.log("Hi" + e);
    //     //setMemberSelected(e.value)
    //     //setPost(e)
    // };

  


    // useEffect(() => {
    //     dispatch( organizationPostsWorkloadDataList(  benchMark, workloadMetric, batchUnit, batchID, batchSize,  dataType  ) )
        
    // }, [dispatch ]);


    const submitHandler = (e) => {
        e.preventDefault();
        //setEditmodel(false);
        // console.log(e);
        console.log(timestamp);
        console.log(benchMark);
        console.log(workloadMetric);
        console.log(batchUnit);
        console.log(batchID);
        console.log(batchSize);
        console.log(dataType);

        dispatch( organizationPostsWorkloadDataList( benchMark, workloadMetric, batchUnit, batchID, batchSize,  dataType  ) )
            // //   dispatch(
            //     organizationPostsWorkloadDataList(
            //         post_id,
            //         requirementInformation,
            //         addressLocation,
            //         MemberSelected
            //     )
            // ); 
        // dispatch(organizationsPostsCreatePost(organizationInfo._id, requirementInformation, organizationInfo.email, addressLocation))
    };

   

    return (
        <div>
            <div style={{ margin: "40px" }}></div>
            <h2> Form for requesting Workload </h2>
            {/*} {error && <Message variant='danger'>{error}</Message>}
        {/* {loading && <Loader />} */}

            {/*} {memberInfo && <Alert  > {memberInfo.username} is registered succesfully</Alert>} */}

            <Form
//  onSubmit={handleChange}              
                className="p-2"
                style={{ "max-width": "95%", margin: "0 auto" }}
            >
                <Form.Group controlId="formGridRFWID" style={{ display: "flex" }}>
                    <Form.Label style={{ width: "30%" }}>RFW Id</Form.Label>

                    <Form.Control
                        type="text"
                        placeholder="_"
                        style={{ width: "70%" }}
                        value={timestamp}
                    />
                </Form.Group>

                <Form.Group controlId="formGridBenchMarKType" style={{ display: "block" }}>
                    <Form.Label style={{ width: "30%" }}>BenchMarK Type : (DVD or NDBENCH)</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Enter BenchMarKType"
                        style={{ width: "70%" }}
                        value={benchMark}
                        onChange={(e) => setBenchMark(e.target.value)}
                    />
                </Form.Group>

                <Form.Group controlId="formGridWorkloadMetric" style={{ display: "block" }}>
                    <Form.Label style={{ width: "100%" }}>Workload Metric : (CPU, NetworkIn, NewtworkOut or Memory)</Form.Label>
                    <Form.Control
                    type="text"
                    placeholder="Enter WorkloadMetric"
                    style={{ width: "70%" }}
                    value={workloadMetric}
                    onChange={(e) => setWorkloadMetric(e.target.value)}
                />
                </Form.Group>

                <Form.Group controlId="formGridBatchUnit" style={{ display: "flex" }}>
                    <Form.Label style={{ width: "30%" }}>Batch Unit :</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Enter Batch Unit"
                        style={{ width: "70%" }}
                        value={batchUnit}
                        onChange={(e) => setBatchUnit(e.target.value)}
                    />
                </Form.Group>
                <Form.Group controlId="formGridBatchID" style={{ display: "flex" }}>
                    <Form.Label style={{ width: "30%" }}>Batch ID :</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Enter Batch ID"
                        style={{ width: "70%" }}
                        value={batchID}
                        onChange={(e) => setBatchID(e.target.value)}
                    />
                </Form.Group>

                <Form.Group
                    controlId="formGridBatchSize"
                    style={{ display: "flex" }}
                >
                    <Form.Label style={{ width: "30%" }}>Batch Size :</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Enter Batch Size "
                        style={{ width: "70%" }}
                        value={batchSize}
                        onChange={(e) => setBatchSize(e.target.value)}
                    />
                </Form.Group>

                <Form.Group
                    controlId="formGridDataType "
                    style={{ display: "block" }}
                >
                    <Form.Label style={{ width: "30%" }}>Data Type : Training or Testing</Form.Label>
                    <Form.Control
                    type="text"
                    placeholder="Enter Data Type"
                    style={{ width: "70%" }}
                    value={dataType}
                    onChange={(e) => setDataType(e.target.value)}
                />
                    
                </Form.Group>
                <Button
                    variant="primary"
                    type="submit"
                    style={{ "background-color": "#4bbf73" }}
                    onClick={submitHandler}
                   >
                    Submit
                </Button>
            </Form>

            {/*
        <Form onSubmit={handleChange} className='my-3 p-2' style={{ 'max-width': '70%', margin: '0 auto' }}>
    
            <Form.Group controlId="formGridUsername" style={{ display: 'flex' }}>
                <Form.Label style={{ width: '30%' }}>RFW Id</Form.Label>
                <Form.Control type="text" placeholder="_" style={{ width: '70%' }}
                    value={'RFW Id '}
                   --onChange={(e) => setUsername(e.target.value)}  --
                    />
            </Form.Group>
            <Form.Group controlId="formGridEmail" style={{ display: 'flex' }}>
                <Form.Label style={{ width: '30%' }}>BenchMarK Type</Form.Label>
                <Select
                                    value={BenchMark}
                                    onChange={(e) => setBenchMark(e.target)} 
                                    options={BenchMarkOptions}
                                />
    
               -- <Form.Control type="email" placeholder="Select Bench Mark" style={{ width: '70%' }}
                    value={email}
                    onChange={(e) => setEmail(e.target.value)} /> --
      </Form.Group>  
    
            <Form.Group controlId="formGridPassword" style={{ display: 'flex' }}>
                <Form.Label style={{ width: '30%' }}>Workload Metric</Form.Label>
                <Select
                value={workloadMetric}
                onChange={(e) => setWorkloadMetric(e.target )} 
                options={workloadMetricOptions}
            />
    
             --   <Form.Control type="password" placeholder="Password" style={{ width: '70%' }}
                    value={password}
                onChange={(e) => setPassword(e.target.value)} /> --
            </Form.Group>
    
    
            <Form.Group controlId="formGridAddressLocation" style={{ display: 'flex' }}>
                <Form.Label style={{ width: '30%' }}>Batch Unit</Form.Label>
                <Form.Control type="text" placeholder="Address Location" style={{ width: '70%' }}
                    value={addressLocation}
                    onChange={(e) => setAddressLocation(e.target.value)} />
            </Form.Group>
    
    
            <Form.Group controlId="formGridAddressLocation" style={{ display: 'flex' }}>
                <Form.Label style={{ width: '30%' }}>Batch ID</Form.Label>
                <Form.Control type="text" placeholder="Address Location" style={{ width: '70%' }}
                    value={addressLocation}
                    onChange={(e) => setAddressLocation(e.target.value)} />
            </Form.Group>
    
            <Form.Group controlId="formGridAddressLocation" style={{ display: 'flex' }}>
                <Form.Label style={{ width: '30%' }}>Batch size</Form.Label>
                <Form.Control type="text" placeholder="Address Location" style={{ width: '70%' }}
                    value={addressLocation}
                    onChange={(e) => setAddressLocation(e.target.value)} />
            </Form.Group>
    
            <Form.Group controlId="formGridAddressLocation" style={{ display: 'flex' }}>
                <Form.Label style={{ width: '30%' }}>Data Type</Form.Label>
                
                <Select
                value={dataType}
                onChange={(e) => setDataType(e.target )} 
                options={dataTypeOptions}
            />
    
               -- <Form.Control type="text" placeholder="Address Location" style={{ width: '70%' }}
                    value={addressLocation}
            onChange={(e) => setAddressLocation(e.target.value)} />   --
            </Form.Group>
    
       
    
            <Alert variant="success" >
                <Alert.Heading>Hey, nice to see you</Alert.Heading>
                <hr />
                <p className="mb-0">
                    Kindly note that details can be updated any time in the update details page. Have a good day!
                </p>
    
            </Alert>
    
            <Button variant="primary" type="submit" style={{ 'background-color': '#4bbf73' }}>
                Submit
            </Button>
    
    
        </Form >



        */}

            <Card className="my-3 p-3 rounded">
                
                <div class="GetOrganizationPosts">
                        {" "}
                        <h2 style={{ textAlign: "center" }}>
                            The Organization Posts Details{" "}
                        </h2>
                        <Table striped bordered hover variant="light">
                            <thead>
                                <tr>
                                    <th style={{ "font-size": "13px" }}>Post Id:</th>
                                    <th style={{ "font-size": "13px" }}>
                                        Organization Requirement Information:
                                    </th>
                                    <th style={{ "font-size": "13px" }}>
                                        Posted by Organization email:
                                    </th>
                                    <th style={{ "font-size": "13px" }}>
                                        Assigned to Member_Id :
                                    </th>
                                    <th style={{ "font-size": "13px" }}> Timeline:</th>
                                </tr>
                            </thead>

                            {organizationPostsWorkLoadDatas.map((organizationPostsWorkLoadData) => (
                                // <Row>

                                //     <Col key={organizationPost._id} sm={12} lg={4} xl={3}>
                                //         <p> Organization Requirement Information: {organizationPost.requirementInformation}  </p>

                                //     </Col>
                                //     <Col key={organizationPost._id} sm={12} lg={4} xl={3}>
                                //         <p> Posted by: {organizationInfo.username}  </p>

                                //     </Col>
                                //     <Col key={organizationPost._id} sm={12} lg={4} xl={3}>
                                //         <p> Assigned to : {organizationPost.MemberSelected_id ? organizationPost.MemberSelected_id : 'None'}  </p>

                                //     </Col>
                                //     <Col key={organizationPost._id} sm={12} lg={4} xl={3}>
                                //         <p> Timeline : <moment >  </moment> </p>

                                //     </Col>

                                // </Row>
                                <tbody>
                                    <tr>
                                        <td key={organizationPostsWorkLoadData._id}>
                                            <p> {organizationPostsWorkLoadData._id} </p>
                                        </td>
                                        <td key={organizationPostsWorkLoadData._id}>
                                            <p> {organizationPostsWorkLoadData.requirementInformation} </p>
                                        </td>
                                        <td key={organizationPostsWorkLoadData._id}>
                                            <p> {organizationPostsWorkLoadData.postedByOrganizationEmail} </p>{" "}
                                        </td>
                                        <td key={organizationPostsWorkLoadData._id}>
                                            <p>
                                                {organizationPostsWorkLoadData.MemberSelected
                                                    ? organizationPostsWorkLoadData.MemberSelected
                                                    : "None"}
                                            </p>
                                        </td>

                                        {/* <td key={organizationPost._id}  >

                                                <input
                                                    type="text"
                                                    placeholder="Company"
                                                    name="company"
                                                    value={organizationPost.MemberSelected}
                                                    onChange={(e) => onChange(e)}
                                                />
                                            </td> */}

                                        <td key={organizationPostsWorkLoadData._id}>
                                            <p>
                                                {moment(organizationPostsWorkLoadData.createdAt).format(
                                                    "DD-MMM-YYYY"
                                                )}
                                            </p>{" "}
                                        </td>
                                        {/*<td key={organizationPostsWorkLoadData._id}>
                                            <p>
                                                <button
                                                    type="button"
                                                    onClick={() => editOrganizationPost(organizationPost)}
                                                >
                                                    Edit Post
                                                </button>
                                            </p>
                                        </td>
                                    
                                    { < h1 hidden (organizationPost.MemberSelected ? i++ : 'NULL) /> */}
                                    </tr>
                                </tbody>
                                // getValueOfI(organizationPost)
                            ))}
                        </Table>
                        <h5
                            className="my-2 p-2"
                            style={{ margin: "0 auto", "text-align": "center" }}
                        >
                            Number of Organization Posts:{" "}
                            {Object.keys(organizationPostsWorkLoadDatas).length}
                        </h5>
                        <h5
                            className="my-2 p-2"
                            style={{ margin: "0 auto", "text-align": "center" }}
                        >
                            {/* Number of Members assigned: {i} */}
                        </h5>
                    </div>
            {/*             )} 

                    //   <Modal show={editModel} onHide={handleClose} animation={false} style={{ top: '20vh' }}>
                  {/*    <Modal.Header closeButton>
                        <Modal.Title style={{ 'max-width': '90%', margin: '0 28px' }} >Organization Post Id: {post_id}</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        {loadingOrganizationPostUpdateList ? <Loader />
                            : errorOrganizationPostUpdateList ? <Message variant='danger'>{errorOrganizationPostUpdateList}</Message> : ''}
                        <Form className='p-2' style={{ 'max-width': '95%', margin: '0 auto' }}>

                            <Form.Group controlId="formGridUsername" style={{ display: 'flex' }}>
                                <Form.Label style={{ width: '30%' }}>Requirement Information:</Form.Label>
                                <Form.Control type="text" placeholder="Enter requirement Information" style={{ width: '70%' }}
                                    value={requirementInformation}
                                    onChange={(e) => setRequirementInformation(e.target.value)} />
                            </Form.Group>
                            <Form.Group controlId="formGridUsername" style={{ display: 'flex' }}>
                                <Form.Label style={{ width: '30%' }}><i class="fas fa-map-marker-alt"></i>  Address Location:</Form.Label>
                                <Form.Control type="text" placeholder="Enter Address Location" style={{ width: '70%' }}
                                    value={addressLocation}
                                    onChange={(e) => setAddressLocation(e.target.value)} />
                            </Form.Group>

                            {/* <Form.Group controlId="formGridMemberSelected" style={{ display: 'flex' }}>
                                <Form.Label style={{ width: '30%' }}>Member Selected_id</Form.Label>
                                <Form.Control type="text" placeholder="Enter Username" style={{ width: '70%' }}
                                    value={MemberSelected}
                                    onChange={(e) => setMemberSelected(e.target.value)} />
                            </Form.Group> 
                            <span>Select Member: </span><Select
                                value={post}
                                onChange={handleChange}
                                options={members && members.map(e => ({ value: e._id, label: e.username + " from " + e.addressLocation }))}
                            />

                        </Form>



                    </Modal.Body>
                    <Modal.Footer>
                        <Button variant="secondary" onClick={handleClose}>
                            Close
                        </Button>
                        <Button variant="primary" onClick={submitHandler}  >
                            Edit Post
                        </Button>
                    </Modal.Footer>
                        </Modal>   */}

                {/*  Use the a href to navigate through other url-> Load a new windows */}
                {/* <Card.body>
               
                 <Card.text as div>
                    <div className='my-3'>
                        {member.name} </div>
                </Card.text> 

           </Card.body>  */}
            </Card>
        </div>
    );
}

export default OrganizationPostsViewPostsScreen;
