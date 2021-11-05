import * as React from "react";
import { StyleSheet } from "react-native";
import { Button as PaperButton } from "react-native-paper";
import useTheme from "../hooks/useTheme";

const Button = ({
  mode,
  style,
  children,
  ...props
}: React.ComponentPropsWithoutRef<typeof PaperButton>) => {
  const theme = useTheme();
  return (
    <PaperButton
      style={[
        styles.button,
        mode === "outlined" && { backgroundColor: theme.colors.surface },
        style,
      ]}
      labelStyle={styles.text}
      mode={mode}
      {...props}
    >
      {children}
    </PaperButton>
  );
};

const styles = StyleSheet.create({
  button: {
    width: "100%",
    marginVertical: 10,
  },
  text: {
    fontWeight: "bold",
    fontSize: 15,
    lineHeight: 26,
  },
});

export default React.memo(Button);
