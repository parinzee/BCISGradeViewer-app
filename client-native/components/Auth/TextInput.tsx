import * as React from "react";
import { StyleSheet, View } from "react-native";
import { TextInput as Input } from "react-native-paper";
import useTheme from "../../hooks/useTheme";

type Props = React.ComponentPropsWithoutRef<typeof Input>;

const TextInput = ({ ...props }: Props) => {
  const theme = useTheme();

  return (
    <View style={styles.container}>
      <Input
        style={{ backgroundColor: theme.colors.surface }}
        selectionColor={theme.colors.primary}
        underlineColor="transparent"
        mode="outlined"
        {...props}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    width: "100%",
    marginVertical: 12,
  },
});

export default TextInput;
