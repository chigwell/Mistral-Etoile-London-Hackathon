import React, { useState, useEffect } from 'react';

import {
  f7,
  f7ready,
  App,
  Panel,
  Views,
  View,
  Popup,
  Page,
  Navbar,
  Toolbar,
  NavRight,
  Link,
  Block,
  BlockTitle,
  List,
  ListItem,
  ListInput,
  ListButton,
  BlockFooter
} from 'framework7-react';


import routes from '../js/routes';

const MyApp = () => {
  // Framework7 Parameters
  const f7params = {
    name: 'Moowee',
    theme: 'md',

    routes: routes,
  };
  f7ready(() => {


    // Call F7 APIs here
  });

  return (
    <App { ...f7params }>

        {/* Left panel with cover effect */}
        <Panel left>
          <View>
            <Page>
              <Navbar title="Menu"/>
                <List dividersIos simpleList strong>
                    <ListItem>
                      <Link
                      view=".view-main"
                      href="/report/" panelClose>Report</Link>
                    </ListItem>
                </List>
                <List dividersIos simpleList strong>
                    <ListItem>
                      <Link
                      view=".view-main"
                      href="/history/" panelClose>History</Link>
                    </ListItem>
                </List>
            </Page>
          </View>
        </Panel>


        {/* Your main view, should have "view-main" class */}
        <View main className="safe-areas" url="/" />

    </App>
  )
}
export default MyApp;