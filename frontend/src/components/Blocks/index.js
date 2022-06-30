import userSVG from '@plone/volto/icons/user.svg';
import homeSVG from '@plone/volto/icons/home.svg';
import PersonBlockViewBlock from './PersonBlock/View';
import PersonBlockEditBlock from './PersonBlock/Edit';
import CampusBlockView from './CampusBlock/View';
import CampusBlockEdit from './CampusBlock/Edit';

const blocks = {
  personBlock: {
    id: 'personBlock',
    title: 'Person Block',
    icon: userSVG,
    group: 'media',
    view: PersonBlockViewBlock,
    edit: PersonBlockEditBlock,
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
  },
  campusBlock: {
    id: 'campusBlock',
    title: 'Campus Block',
    icon: homeSVG,
    group: 'media',
    view: CampusBlockView,
    edit: CampusBlockEdit,
    restricted: false,
    mostUsed: false,
    sidebarTab: 1,
  },
};

export default blocks;
