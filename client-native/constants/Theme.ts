import {
  DarkTheme as NavigationDarkTheme,
  DefaultTheme as NavigationDefaultTheme,
} from '@react-navigation/native';
import {
  DarkTheme as PaperDarkTheme,
  DefaultTheme as PaperDefaultTheme,
} from 'react-native-paper';
import merge from 'deepmerge';

export const LightTheme = merge(PaperDefaultTheme, NavigationDefaultTheme);
export const DarkTheme = merge(PaperDarkTheme, NavigationDarkTheme);
