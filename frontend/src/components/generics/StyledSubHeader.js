import styled from "vue-styled-components";
import ReadStyleGuide from "../../styles/ReadStyleGuide";
import { themeProps } from "./ThemeProps";
import { media } from "./MediaSizes";

export const StyledSubHeader = styled("h2", themeProps)`
  width: ${props => props.width || "initial"};
  text-align: ${props => props.textAlign || "center"};
  margin: ${props => props.margin || "0px"};
  color: ${props => props.color || ReadStyleGuide.color.darkBlue};
  padding: ${props => props.padding || "0 2%"};
  font-family: ${props => props.fontFamily || ReadStyleGuide.font.family.chivo};
  font-size: ${props => props.fontSize || ReadStyleGuide.font.size.medium};
  white-space: ${props => props.whiteSpace || "pre-line"};
  line-height: ${props => props.lineHeight || "initial"};
  ${props => (props.fontStyle ? `font-style: ${props.fontStyle}` : null)};
  ${props => (props.fontWeight ? `font-weight:${props.fontWeight}` : null)};
  ${props =>
    props.textDecoration ? `text-decoration:${props.textDecoration}` : null};

  &:hover {
    color: ${props => props.hoverColor || null};
    cursor: ${props => props.cursorType || null};
}

  ${media.desktop`font-size: ${props => props.desktopFontSize || null};`}
  ${media.tablet`font-size: ${props => props.tabletFontSize || null};`}
  ${media.phone`font-size: ${props => props.phoneFontSize || null};`}
`;
