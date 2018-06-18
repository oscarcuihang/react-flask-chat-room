import React from 'react';
import ReactDOM from 'react-dom';
import { Button } from 'element-react';
import 'element-theme-default';

export default class App extends React.Component {
  render () {
    return (
      <div>
        <h1> Hello App </h1>
        <Button type='primary'>Hello</Button>
      </div>
    );
  }
}
