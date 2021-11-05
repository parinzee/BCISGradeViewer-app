import * as React from "react";
import { StyleSheet, Text, View } from "react-native";
import useTheme from "../../hooks/useTheme";

type Props = {
  children: React.ReactNode;
};

const Header = ({ children }: Props) => {
  const theme = useTheme();
  return (
    <View>
      <Text style={{ ...styles.header, color: theme.colors.primary }}>
        {children}
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
  header: {
    fontSize: 26,
    fontWeight: "bold",
    paddingVertical: 14,
  },
});

export default React.memo(Header);
