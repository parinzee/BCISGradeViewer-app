import * as React from "react";
import {
  ImageBackground,
  StyleSheet,
  KeyboardAvoidingView,
  Keyboard,
  Pressable,
} from "react-native";

type Props = {
  children: React.ReactNode;
};

const Background = ({ children }: Props) => {
  return (
    <ImageBackground
      source={require("../../assets/images/dot.png")}
      resizeMode="repeat"
      style={styles.background}
    >
      <KeyboardAvoidingView style={styles.container} behavior="padding">
        <Pressable
          onPress={() => {
            Keyboard.dismiss();
          }}
          style={styles.pressable}
        >
          {children}
        </Pressable>
      </KeyboardAvoidingView>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
  background: {
    flex: 1,
    width: "100%",
  },
  container: {
    flex: 1,
    padding: 20,
    width: "100%",
    maxWidth: 350,
    alignSelf: "center",
    alignItems: "center",
    justifyContent: "center",
  },
  pressable: {
    flex: 1,
    width: "100%",
    alignSelf: "center",
    alignItems: "center",
    justifyContent: "center",
  },
});

export default React.memo(Background);
