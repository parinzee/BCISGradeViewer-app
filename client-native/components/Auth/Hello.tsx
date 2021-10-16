import * as React from "react";
import LottieView from "lottie-react-native";

const Hello = () => {
  return (
    <LottieView
      source={require("../../assets/images/hello.json")}
      autoPlay
      loop={false}
      style={{ height: 250 }}
    />
  );
};

export default Hello;
