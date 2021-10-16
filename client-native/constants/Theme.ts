import {
  DarkTheme as NavigationDarkTheme,
  DefaultTheme as NavigationDefaultTheme,
} from '@react-navigation/native';
import {
  DarkTheme as PaperDarkTheme,
  DefaultTheme as PaperDefaultTheme,
} from 'react-native-paper';
import merge from 'deepmerge';

const newPaperDefault = {
  ...PaperDefaultTheme,
  colors: {
    ...PaperDefaultTheme.colors,
    primary: '#600EE6',
    secondary: '#414757',
    error: '#f13a59',
  }
}


const newPaperDark = {
  ...PaperDarkTheme,
  colors: {
    ...PaperDarkTheme.colors,
    primary: '#600EE6',
    secondary: '#414757',
    error: '#f13a59',
  }
}

export const LightTheme = merge(NavigationDefaultTheme, newPaperDefault);
export const DarkTheme = merge(NavigationDefaultTheme, newPaperDark);
