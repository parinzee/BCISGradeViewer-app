import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import React from "react";

import { RootStackParamList } from "./types";
import LinkingConfiguration from "./LinkingConfiguration";
import useTheme from "../hooks/useTheme";

import Auth from "../screens/Auth";

export default function Navigation() {
  const theme = useTheme();
  return (
    <NavigationContainer linking={LinkingConfiguration} theme={theme}>
      <RootNavigator />
    </NavigationContainer>
  );
}

const Stack = createNativeStackNavigator<RootStackParamList>();

function RootNavigator() {
  return (
    <Stack.Navigator>
      <Stack.Screen
        name="Auth"
        component={Auth}
        options={{ title: "Welcome!" }}
      />
    </Stack.Navigator>
  );
}
