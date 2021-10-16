import { LightTheme, DarkTheme } from '../constants/Theme';
import { useColorScheme } from 'react-native';

export default function useTheme(): typeof LightTheme {
    const colorScheme = useColorScheme();
    if (colorScheme === "dark") {
        return DarkTheme
    } else {
        return LightTheme
    }

}