class Header extends HTMLElement {
    connectedCallback() {
      this.innerHTML = `          
      <div class="navig">
            <a href="lp.html"><img class="logo" src="assets/navbar/logo.png"></a>
             <nav>
                 <ul>
                      <li><a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q"><img class="spot" src="assets/navbar/spotify.png"></a></li>
                      <li><a href="https://www.youtube.com/@ImagineDragons"><img src="assets/navbar/youtube.svg"></a></li>
                     <li><a href="https://twitter.com/Imaginedragons?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"><img src="assets/navbar/twitter.svg"></a></li>
                     <li><a href="https://www.instagram.com/imaginedragons/?hl=en"><img src="assets/navbar/instagram.svg"></a></li>
                </ul>
             </nav>
      </div>
      `;
    }
  }

  customElements.define('main-header', Header);