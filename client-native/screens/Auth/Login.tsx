import * as React from "react";
import Background from "../../components/Auth/Background";
import Hello from "../../components/Auth/Hello";
import TextInput from "../../components/Auth/TextInput";

export default function Login() {
  return (
    <Background>
      <Hello />
      <TextInput />
    </Background>
  );
}
