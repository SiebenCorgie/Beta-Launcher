# Maintainer: Your Name officialsiebencorgie@gmail.com>
pkgname=beta-launcher
pkgver=0.2_1
pkgrel=1
pkgdesc="Launcher programm to manage and install UE4 on Linux"
arch=("any")
url="https://forums.unrealengine.com/showthread.php?110795-Beta-Launcher-for-Linux&p=534937#post534937"
license=("GPL3")
depends=("pywebkitgtk" "webkitgtk" "pygtk" "vte3" "vte-common" "git")
backup=("etc/beta-launcher/defaults.conf" "etc/beta-launcher/settings.conf")
options=()
install=
changelog="ChangeLog"
source=("git+https://github.com/SiebenCorgie/Beta-Launcher.git#branch=version-0.2")
md5sums=("SKIP")

package() {

	#creating main programm directory and copy everything in there
	mkdir -p "$pkgdir/usr/share/beta-launcher"
	cp -af "Beta-Launcher/." "$pkgdir/usr/share/beta-launcher"
	cd "$pkgdir/usr/share/beta-launcher"

	#Install .desktop entry, icons and the starter script
	install -Dm644 "beta-launcher.desktop" "$pkgdir/usr/share/applications/beta-launcher.desktop"
	install -Dm644 "src/pixmaps/beta-launcher.png" "$pkgdir/usr/share/pixmaps/beta-launcher.png"
	install -Dm755 "$srcdir/Beta-Launcher/beta-launcher" "$pkgdir/usr/bin/beta-launcher"

	#adding default configruation files to /etc/beta-launcher
	mkdir -p "$pkgdir/etc/beta-launcher/"
	cd "$pkgdir/usr/share/beta-launcher"
	install -Dm666 "settings.conf" "$pkgdir/etc/beta-launcher/settings.conf"
	install -Dm666 "defaults.conf" "$pkgdir/etc/beta-launcher/defaults.conf"
}
