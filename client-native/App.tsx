import { StatusBar } from "expo-status-bar";
import React from "react";
import { SafeAreaProvider } from "react-native-safe-area-context";

import useCachedResources from "./hooks/useCachedResources";
import useTheme from "./hooks/useTheme";
import Navigation from "./navigation";
import { Provider as PaperProvider } from "react-native-paper";

export default function App() {
  const isLoadingComplete = useCachedResources();
  const theme = useTheme();

  if (!isLoadingComplete) {
    return null;
  } else {
    return (
      <SafeAreaProvider>
        <PaperProvider theme={theme}>
          <Navigation />
          <StatusBar />
        </PaperProvider>
      </SafeAreaProvider>
    );
  }
}
