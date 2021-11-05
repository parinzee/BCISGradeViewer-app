import * as React from "react";
import Background from "../../components/Auth/Background";
import Hello from "../../components/Auth/Hello";
import Header from "../../components/Auth/Header";
import TextInput from "../../components/Auth/TextInput";
import Button from "../../components/Button";

export default function Login() {
  const [username, setUsername] = React.useState("");
  const [password, setPassword] = React.useState("");
  return (
    <Background>
      <Hello />
      <Header>Welcome Back!</Header>
      <TextInput
        label="Username"
        returnKeyType="next"
        value={username}
        onChangeText={setUsername}
        autoCapitalize="none"
        secureTextEntry={false}
      />
      <TextInput
        label="Password"
        returnKeyType="done"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <Button mode="contained">Login</Button>
    </Background>
  );
}
