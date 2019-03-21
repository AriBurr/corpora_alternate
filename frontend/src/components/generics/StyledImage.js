import styled from "vue-styled-components";
import themeProps from "./ThemeProps";
import { media } from "./MediaSizes";

export const StyledImage = styled("img", themeProps)`
max-width: ${props => props.maxWidth};
max-height: ${props => props.maxHeight};
min-width: ${props => props.minWidth || null};
min-height: ${props => props.minHeight || null};
width: ${props => props.width || "100%"};
height: ${props => props.height || "100%"};
border-radius: ${props => props.borderRadius || "0px"};
box-shadow: ${props => props.boxShadow};
padding: ${props => props.padding || null};
margin: ${props => props.margin || null};

  ${media.desktop`height: 
    ${props => props.desktopHeight};
  `} 
  ${media.tablet`height:
    ${props => props.tabletHeight}
  `} 
  ${media.phone`height: 
    ${props => props.phoneHeight}
  `};
`;
