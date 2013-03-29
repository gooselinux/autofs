#
# $Id: autofs.spec,v 1.11 2003/12/04 15:41:32 raven Exp $
#
Summary: A tool for automatically mounting and unmounting filesystems
Name: autofs
Version: 5.0.5
Release: 23%{?dist}.1
Epoch: 1
License: GPLv2+
Group: System Environment/Daemons
URL: http://wiki.autofs.net/
Source: ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/autofs-%{version}.tar.bz2
Patch1: autofs-5.0.5-fix-included-map-read-fail-handling.patch
Patch2: autofs-5.0.5-refactor-ldap-sasl-bind.patch
Patch3: autofs-5.0.4-add-mount-wait-parameter.patch
Patch4: autofs-5.0.5-special-case-cifs-escapes.patch
Patch5: autofs-5.0.5-fix-libxml2-workaround-configure.patch
Patch6: autofs-5.0.5-more-code-analysis-corrections.patch
Patch7: autofs-5.0.5-fix-backwards-ifndef-INET6.patch
Patch8: autofs-5.0.5-fix-stale-init-for-file-map-instance.patch
Patch9: autofs-5.0.5-fix-ext4-fsck-at-mount.patch
Patch10: autofs-5.0.5-dont-use-master_lex_destroy-to-clear-parse-buffer.patch
Patch11: autofs-5.0.5-make-documentation-for-set-log-priority-clearer.patch
Patch12: autofs-5.0.5-fix-timeout-in-connect_nb.patch
Patch13: autofs-5.0.5-fix-pidof-init-script-usage.patch
Patch14: autofs-5.0.5-check-for-path-mount-location-in-generic-module.patch
Patch15: autofs-5.0.5-dont-fail-mount-on-access-fail.patch
Patch16: autofs-5.0.5-fix-rpc-large-export-list.patch
Patch17: autofs-5.0.5-dont-connect-at-ldap-lookup-module-init.patch
Patch18: autofs-5.0.5-fix-reconnect-get-base-dn.patch
Patch19: autofs-5.0.5-fix-random-selection-option.patch
Patch20: autofs-5.0.5-fix-disable-timeout.patch
Patch21: autofs-5.0.5-fix-strdup-return-value-check.patch
Patch22: autofs-5.0.5-fix-get-qdn-fail.patch
Patch23: autofs-5.0.5-fix-ampersand-escape-in-auto-smb.patch
Patch24: autofs-5.0.5-make-nfs4-default-for-redhat-replicated-selection.patch
Patch25: autofs-5.0.5-add-autofs_ldap_auth_conf-man-page.patch
Patch26: autofs-5.0.5-fix-random-selection-for-host-on-different-network.patch
Patch27: autofs-5.0.5-make-redhat-init-script-more-lsb-compliant.patch
Patch28: autofs-5.0.5-add-sasl-mutex-callbacks.patch
Patch29: autofs-5.0.5-fix-parse_sun-module-init.patch
Patch30: autofs-5.0.5-dont-check-null-cache-on-expire.patch
Patch31: autofs-5.0.5-fix-null-cache-race.patch
Patch32: autofs-5.0.5-fix-cache_init-on-source-re-read.patch
Patch33: autofs-5.0.5-fix-negative-cache-included-map-lookup.patch
Patch34: autofs-5.0.5-fix-remount-locking.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: autoconf, hesiod-devel, openldap-devel, bison, flex, libxml2-devel, cyrus-sasl-devel, openssl-devel module-init-tools util-linux nfs-utils e2fsprogs libtirpc-devel
Conflicts: cyrus-sasl-lib < 2.1.23-7
Requires: kernel >= 2.6.17
Requires: bash mktemp sed gawk textutils sh-utils grep module-init-tools /bin/ps
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service
Requires(postun): /sbin/chkconfig
Summary(de): autofs daemon 
Summary(fr): démon autofs
Summary(tr): autofs sunucu süreci
Summary(sv): autofs-daemon

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%description -l de
autofs ist ein Dämon, der Dateisysteme automatisch montiert, wenn sie 
benutzt werden, und sie später bei Nichtbenutzung wieder demontiert. 
Dies kann Netz-Dateisysteme, CD-ROMs, Disketten und ähnliches einschließen. 

%description -l fr
autofs est un démon qui monte automatiquement les systèmes de fichiers
lorsqu'on les utilise et les démonte lorsqu'on ne les utilise plus. Cela
inclus les systèmes de fichiers réseau, les CD-ROMs, les disquettes, etc.

%description -l tr
autofs, kullanýlan dosya sistemlerini gerek olunca kendiliðinden baðlar
ve kullanýmlarý sona erince yine kendiliðinden çözer. Bu iþlem, að dosya
sistemleri, CD-ROM'lar ve disketler üzerinde yapýlabilir.

%description -l sv
autofs är en daemon som mountar filsystem när de använda, och senare
unmountar dem när de har varit oanvända en bestämd tid.  Detta kan
inkludera nätfilsystem, CD-ROM, floppydiskar, och så vidare.

%prep
%setup -q
echo %{version}-%{release} > .version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1

%build
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --libdir=%{_libdir}
%configure --disable-mount-locking --enable-ignore-busy --with-libtirpc
make initdir=%{_initrddir} DONTSTRIP=1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m755 $RPM_BUILD_ROOT%{_initrddir}
mkdir -p -m755 $RPM_BUILD_ROOT%{_sbindir}
mkdir -p -m755 $RPM_BUILD_ROOT%{_libdir}/autofs
mkdir -p -m755 $RPM_BUILD_ROOT%{_mandir}/{man5,man8}
mkdir -p -m755 $RPM_BUILD_ROOT/etc/sysconfig

make install mandir=%{_mandir} initdir=%{_initrddir} INSTALLROOT=$RPM_BUILD_ROOT
make -C redhat
install -m 755 -d $RPM_BUILD_ROOT/misc
install -m 755 redhat/autofs.init $RPM_BUILD_ROOT%{_initrddir}/autofs
install -m 644 redhat/autofs.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/autofs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add autofs

%postun
if [ $1 -ge 1 ] ; then
    /sbin/service autofs condrestart > /dev/null 2>&1 || :
fi

%preun
if [ "$1" = 0 ] ; then
    /sbin/service autofs stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del autofs
fi

%files
%defattr(-,root,root,-)
%doc CREDITS INSTALL COPY* README* patches/* samples/ldap* samples/autofs.schema
%{_initrddir}/autofs
%config(noreplace,missingok) /etc/auto.master
%config(noreplace,missingok) /etc/auto.misc
%config(noreplace,missingok) /etc/auto.net
%config(noreplace,missingok) /etc/auto.smb
%config(noreplace) /etc/sysconfig/autofs
%config(noreplace) /etc/autofs_ldap_auth.conf
%{_sbindir}/automount
%{_mandir}/*/*
%{_libdir}/autofs/

%changelog
* Tue Mar 22 2011 Ian Kent <ikent@redhat.com> - 5.0.5-23.el6_0.1
- bz689754 - automount hangs on startup when started with an already
  mounted cifs share
  - fix remount locking
- Resolves: rhbz#689754

* Thu Jul 1 2010 Ian Kent <ikent@redhat.com> - 5.0.5-23
- bz597944 - autofs5: segfault in close_mount()
  - add mutex to serialize access to mount module handle in parse module.
  - dont check null cache on expire.
  - fix null cache race.
  - fix cache_init() on source re-read.
  - fold autofs-5.0.5-fix-memory-leak-on-reload.patch into
    fix cache_init() on source re-read patch where it belongs.
- bz594565 - If maps include both file and nis maps, included nis maps which
    worked on RHEL 5.3 no longer work on RHEL 5.4
  - fix negative cache included map lookup
- Resolves: rhhz#597944 rhbz#594565

* Thu Jun 3 2010 Ian Kent <kpnt@redhat.com> - 1:5.0.5-22
- bz578128 - Service autofs initscript not LSB compliant
- bz577097 - automount aborts when it authenticates by DIGEST-MD5
- Resolves: rhbz#578128 rhbz#577097

* Thu Apr 8 2010 Ian Kent <kpnt@redhat.com> - 1:5.0.5-21
-bz578677 - random server selection is not random if any host is on a different network
 - fix random selection for host on different network
- Resolves: rhbz#578677

* Wed Apr 7 2010 Ian Kent <kpnt@redhat.com> - 1:5.0.5-20
- bz529347 - Missing man-pages.
  - add autofs_ldap_auth.conf man page.
- Resolves: rhbz#529347

* Mon Mar 29 2010 Ian Kent <kpnt@redhat.com> - 1:5.0.5-19
- bz563769 - [RFE] autofs needs to wait for a network up event before starting
  - fix get query dn failure
- bz574309 - autofs cannot mount the folder name including "&"
  - fix ampersand escape in auto.smb.
- bz465463 - CRM 1203376 autofs/automount to mount nfs4 or nfs3 for mixed servers
  - make nfs4 default for RedHat replicated selection configuration.
- Resolves: rhbz#574309 rhbz#465463
- Related: rhbz#563769

* Wed Mar 3 2010 Ian Kent <kpnt@redhat.com> - 1:5.0.5-18
- bz563769 - [RFE] autofs needs to wait for a network up event before starting
  - dont connect at ldap lookup module init.
  - fix reconnect get base dn.
- bz563772 - automount cannot use rpc ping to select from list of replicated servers
  - fix random selection option.
- bz563773 - [RHEL 5] RHEL5.4 TIMEOUT=0 automount constantly unmount fileystems
  - fix disable timeout.
- bz563777 - Incorrect strdup() return value check in lib/defaults.c:get_env_string()
  - fix strdup() return value check.
- Resolves: rhbz#563769 rhbz#563772 rhbz#563773 rhbz#563777

* Tue Dec 8 2009 Ian Kent <kpnt@redhat.com> - 1:5.0.5-17
- fix memory leak on reload (bz545137).

* Thu Dec 3 2009 Ian Kent <kpnt@redhat.com> - 1:5.0.5-15
- fix rpc fail on large export list (bz543023).

* Mon Nov 30 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-13
- check for path mount location in generic module.
- dont fail mount on access fail.

* Wed Nov 25 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-11
- fix pidof init script usage.

* Mon Nov 23 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-9
- fix timeout in connect_nb().

* Mon Nov 16 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-7
- fix ext4 "preen" fsck at mount.
- don't use master_lex_destroy() to clear parse buffer.
- make documentation for set-log-priority clearer.

* Tue Nov 3 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-4
- fix included map read fail handling.
- refactor ldap sasl authentication bind to eliminate extra connect
  causing some servers to reject the request.
- add mount wait parameter to allow timeout of mount requests to
  unresponsive servers.
- special case cifs escape handling.
- fix libxml2 workaround configure.
- more code analysis corrections (and fix a typo in an init script).
- fix backwards #ifndef INET6.
- fix stale initialization for file map instance.

* Fri Sep 4 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-1
- update source to latest upstream version.
  - this is essentially a consolidation of the patches already in this rpm.
- add dist tag to match latest RHEL-5 package tag format.

* Thu Sep 3 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-39
- fix libxml2 non-thread-safe calls.
- fix direct map cache locking.
- fix patch "dont umount existing direct mount on reread" deadlock.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-34
- fix typo in patch to allow dumping core.

* Wed Jul 15 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-32
- fix an RPC fd leak.
- don't block signals we expect to dump core.
- fix pthread push order in expire_proc_direct().

* Fri Jun 12 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-30
- fix incorrect dclist free.
- srv lookup handle endianness.
- fix bug introduced by library reload changes which causes autofs to
  not release mount thread resources when using submounts.
- fix notify mount message path.
- try harder to work out if we created mount point at remount.
- fix double free in do_sasl_bind().
- manual umount recovery fixes.
- fix map type info parse error.

* Mon May 18 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-28
- use intr option as hosts mount default.
- sync kernel includes with upstream kernel.
- dont umount existing direct mount on master re-read.
- fix incorrect shutdown introduced by library relaod fixes.
- improve manual umount recovery.
- dont fail on ipv6 address when adding host.
- always read file maps multi map fix.
- always read file maps key lookup fixes.
- add support for LDAP_URI="ldap:///<domain db>" SRV RR lookup.

* Thu Apr 16 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-26
- fix lsb init script header.
- fix memory leak reading ldap master map.
- fix st_remove_tasks() locking.
- reset flex scanner when setting buffer.
- zero s_magic is valid.

* Mon Mar 30 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-24
- clear rpc client on lookup fail.

* Fri Mar 20 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-23
- fix call restorecon when misc device file doesn't exist.

* Wed Mar 18 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-22
- use misc device ioctl interface by default, if available.

* Tue Mar 17 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-21
- fix file map lookup when reading included or nsswitch sources.
  - a regression introduced by file map lookup optimisation in rev 9.

* Fri Mar 13 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-20
- add LSB init script parameter block.

* Fri Mar 13 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-19
- another easy alloca replacements fix.

* Thu Mar 12 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-18
- fix return start status on fail.
- fix double free in expire_proc().

* Wed Feb 25 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-17
- fix bad token declaration in master map parser.

* Wed Feb 25 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-16
- correct mkdir command in %%install section, bz481132.

* Tue Feb 24 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-15
- fix array out of bounds accesses and cleanup couple of other alloca() calls.
- Undo mistake in copy order for submount path introduced by rev 11 patch.
- add check for alternate libxml2 library for libxml2 tsd workaround.
- add check for alternate libtirpc library for libtirpc tsd workaround.
- cleanup configure defines for libtirpc.
- add WITH_LIBTIRPC to -V status report.
- add libtirpc-devel to BuildRequires.
- add nfs mount protocol default configuration option.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Ian Kent <ikent@redhat.com> - 5.0.4-10
- fix mntent.h not included before use of setmntent_r().

* Mon Feb 16 2009 Ian Kent <ikent@redhat.com> - 5.0.4-9
- fix hosts map use after free.
- fix uri list locking (again).
- check for stale SASL credentials upon connect fail.
- add "forcestart" and "forcerestart" init script options to allow
  use of 5.0.3 strartup behavior if required.
- always read entire file map into cache to speed lookups.
- make MAX_ERR_BUF and PARSE_MAX_BUF use easier to audit.
- make some easy alloca replacements.
- update to configure libtirpc if present.
- update to provide ipv6 name and address support.
- update to provide ipv6 address parsing.

* Thu Feb 5 2009 Ian Kent <ikent@redhat.com> - 5.0.4-8
- rename program map parsing bug fix patch.
- use CLOEXEC flag functionality for setmntent also, if present.

* Wed Jan 21 2009 Jeff Moyer <jmoyer@redhat.com> - 5.0.4-6
- fix a bug in the program map parsing routine

* Thu Jan 15 2009 Ian Kent <kent@redhat.com> - 5.0.4-5
- fix negative caching of non-existent keys.
- fix ldap library detection in configure.
- use CLOEXEC flag functionality if present.
- fix select(2) fd limit.
- make hash table scale to thousands of entries.

* Wed Dec 3 2008 Ian Kent <kent@redhat.com> - 5.0.4-4
- fix nested submount expire deadlock.

* Wed Nov 19 2008 Ian Kent <kent@redhat.com> - 5.0.4-3
- fix libxml2 version check for deciding whether to use workaround.

* Tue Nov 11 2008 Ian Kent <kent@redhat.com> - 5.0.4-2
- Fix tag confusion.

* Tue Nov 11 2008 Ian Kent <kent@redhat.com> - 5.0.4-1
- Upstream source version 5.0.4.

* Tue Nov 11 2008 Ian Kent <kent@redhat.com> - 5.0.3-32
- correct buffer length setting in autofs-5.0.3-fix-ifc-buff-size-fix.patch.

* Sun Nov 2 2008 Ian Kent <kent@redhat.com> - 5.0.3-30
- fix segv during library re-open.
- fix incorrect pthreads condition handling for expire requests.
- fix master map lexer eval order.
- fix bad alloca usage.

* Thu Oct 23 2008 Ian Kent <ikent@redhat.com> - 5.0.3-28
- don't close file handle for rootless direct mounti-mount at mount.
- wait submount expire thread completion when expire successful.
- add inadvertantly ommitted server list locking in LDAP module.

* Fri Oct 10 2008 Ian Kent <ikent@redhat.com> - 5.0.3-26
- add map-type-in-map-name fix patch to sync with upstream and RHEL.
- don't readmap on HUP for new mount.
- add NIS_PARTIAL to map entry not found check and fix use after free bug.

* Fri Sep 26 2008 Ian Kent <ikent@redhat.com> - 5.0.3-25
- fix fd leak at multi-mount non-fatal mount fail.
- fix incorrect multi-mount mountpoint calcualtion.

* Fri Sep 19 2008 Ian Kent <ikent@redhat.com> - 5.0.3-23
- add upstream bug fixes
  - bug fix for mtab check.
  - bug fix for zero length nis key.
  - update for ifc buffer handling.
  - bug fix for kernel automount handling.
- warning: I found a bunch of patches that were present but not
  being applied.
  
* Mon Aug 25 2008 Ian Kent <ikent@redhat.com> - 5.0.3-21
- add upstream bug fix patches
  - add command line option to override is running check.
  - don't use proc fs for is running check.
  - fix fail on included browse map not found.
  - fix incorrect multi source messages.
  - clear stale flag on map read.
  - fix proximity other rpc ping timeout.
  - refactor mount request vars code.
  - make handle_mounts startup condition distinct.
  - fix submount shutdown handling.
  - try not to block on expire.
  - add configuration paramter UMOUNT_WAIT.
  - fix multi mount race.
  - fix nfs4 colon escape handling.
  - check replicated list after probe.
  - add replicated server selection debug logging.
  - update replicated server selection documentation.
  - use /dev/urandom instead of /dev/random.
  - check for mtab pointing to /proc/mounts.
  - fix interface config buffer size.
  - fix percent hack heap corruption.

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.0.3-19
- change conflicts to requires
- fix license tag

* Mon Jun 30 2008 Ian Kent <ikent@redhat.com> - 5.0.3-18
- don't abuse the ap->ghost field on NFS mount.
- multi-map doesn't pickup NIS updates automatically.
- eliminate redundant DNS name lookups.
- mount thread create condition handling fix.
- allow directory create on NFS root.
- check direct mount path length.
- fix incorrect in check in get user info.
- fix a couple of memory leaks.

* Wed May 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-16
- update patches, documentation and comments only change.
- rename patch and add to CVS.

* Mon May 12 2008 Ian Kent <ikent@redhat.com> - 5.0.3-14
- check for nohide mounts (bz 442618).
- ignore nsswitch sources that aren't supported (bz 445880).

* Thu Apr 17 2008 Ian Kent <ikent@redhat.com> - 5.0.3-13
- fix typo in patch for incorrect pthreads condition handling patch.

* Mon Apr 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-12
- fix incorrect pthreads condition handling for mount requests.

* Sun Apr 1 2008 Ian Kent <ikent@redhat.com> - 5.0.3-11
- and another try at fixing lexer matching map type in map name.

* Sun Mar 30 2008 Ian Kent <ikent@redhat.com> - 5.0.3-10
- another try a fixing lexer matching map type in map name.

* Wed Mar 26 2008 Ian Kent <ikent@redhat.com> - 5.0.3-9
- fix lexer ambiguity in match when map type name is included in map name.

* Mon Mar 24 2008 Ian Kent <ikent@redhat.com> - 5.0.3-8
- revert miscellaneous device node related patches.
- add missing check for zero length NIS key.
- fix incorrect match of map type name when included in map name.
- update rev 7 sasl callbacks patch.

* Thu Mar 20 2008 Ian Kent <ikent@redhat.com> - 5.0.3-7
- add patch to initialize sasl callbacks unconditionally on autofs
  LDAP lookup library load.

* Mon Feb 25 2008 Ian Kent <ikent@redhat.com> - 5.0.3-6
- fix expire calling kernel more often than needed.
- fix unlink of mount tree incorrectly causing autofs mount fail.
- add miscellaneous device node interface library.
- use miscellaneous device node, if available, for active restart.
- device node and active restart fixes.
- update is_mounted to use device node ioctl, if available.

* Fri Feb 1 2008 Ian Kent <ikent@redhat.com> - 5.0.3-5
- another fix for don't fail on empty master map.

* Fri Jan 25 2008 Ian Kent <ikent@redhat.com> - 5.0.3-4
- correction to the correction for handling of LDAP base dns with spaces.
- avoid using UDP for probing NFSv4 mount requests.
- use libldap instead of libldap_r.

* Mon Jan 21 2008 Ian Kent <ikent@redhat.com> - 5.0.3-3
- catch "-xfn" map type and issue "no supported" message.
- another correction for handling of LDAP base dns with spaces.

* Mon Jan 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-2
- correct configure test for ldap page control functions.

* Mon Jan 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-1
- update source to version 5.0.3.

* Fri Dec 21 2007 Ian Kent <ikent@redhat.com> - 5.0.2-25
- Bug 426401: CVE-2007-6285 autofs default doesn't set nodev in /net [rawhide]
  - use mount option "nodev" for "-hosts" map unless "dev" is explicily specified.

* Tue Dec 18 2007 Ian Kent <ikent@redhat.com> - 5.0.2-23
- Bug 397591 SELinux is preventing /sbin/rpc.statd (rpcd_t) "search" to <Unknown> (sysctl_fs_t).
  - prevent fork between fd open and setting of FD_CLOEXEC.

* Thu Dec 13 2007 Ian Kent <ikent@redhat.com> - 5.0.2-21
- Bug 421371: CVE-2007-5964 autofs defaults don't restrict suid in /net [rawhide]
  - use mount option "nosuid" for "-hosts" map unless "suid" is explicily specified.

* Thu Dec  6 2007 Jeremy Katz <katzj@redhat.com> - 1:5.0.2-19
- rebuild for new ldap

* Tue Nov 20 2007 Ian Kent <ikent@redhat.com> - 5.0.2-18
- fix schema selection in LDAP schema discovery.
- check for "*" when looking up wildcard in LDAP.
- fix couple of edge case parse fails of timeout option.
- add SEARCH_BASE configuration option.
- add random selection as a master map entry option.
- re-read config on HUP signal.
- add LDAP_URI, LDAP_TIMEOUT and LDAP_NETWORK_TIMEOUT configuration options.
- fix deadlock in submount mount module.
- fix lack of ferror() checking when reading files.
- fix typo in autofs(5) man page.
- fix map entry expansion when undefined macro is present.
- remove unused export validation code.
- add dynamic logging (adapted from v4 patch from Jeff Moyer).
- fix recursive loopback mounts (Matthias Koenig).
- add map re-load to verbose logging.
- fix handling of LDAP base dns with spaces.
- handle MTAB_NOTUPDATED status return from mount.
- when default master map, auto.master, is used also check for auto_master.
- update negative mount timeout handling.
- fix large group handling (Ryan Thomas).
- fix for dynamic logging breaking non-sasl build (Guillaume Rousse).
- eliminate NULL proc ping for singleton host or local mounts.

* Mon Sep 24 2007 Ian Kent <ikent@redhat.com> - 5.0.2-16
- add descriptive comments to config about LDAP schema discovery.
- work around segfault at exit caused by libxml2.
- fix foreground logging (also fixes shutdown needing extra signal bug).

* Wed Sep 5 2007 Ian Kent <ikent@redhat.com> - 5.0.2-15
- fix LDAP schema discovery.

* Tue Aug 28 2007 Ian Kent <ikent@redhat.com> - 5.0.2-14
- update patch to prevent failure on empty master map.
- if there's no "automount" entry in nsswitch.conf use "files" source.
- add LDAP schema discovery if no schema is configured.

* Wed Aug 22 2007 Ian Kent <ikent@redhat.com> - 5.0.2-13
- fix "nosymlink" option handling and add desription to man page.

* Tue Aug 21 2007 Ian Kent <ikent@redhat.com> - 5.0.2-12
- change random multiple server selection option name to be consistent
  with upstream naming.

* Tue Aug 21 2007 Ian Kent <ikent@redhat.com> - 5.0.2-11
- don't fail on empty master map.
- add support for the "%" hack for case insensitive attribute schemas.

* Mon Jul 30 2007 Ian Kent <ikent@redhat.com> - 5.0.2-10
- mark map instances stale so they aren't "cleaned" during updates.
- fix large file compile time option.

* Fri Jul 27 2007 Ian Kent <ikent@redhat.com> - 5.0.2-9
- fix version passed to get_supported_ver_and_cost (bz 249574).

* Tue Jul 24 2007 Ian Kent <ikent@redhat.com> - 5.0.2-8
- fix parse confusion between attribute and attribute value.

* Fri Jul 20 2007 Ian Kent <ikent@redhat.com> - 5.0.2-7
- fix handling of quoted slash alone (bz 248943).

* Wed Jul 18 2007 Ian Kent <ikent@redhat.com> - 5.0.2-6
- fix wait time resolution in alarm and state queue handlers (bz 247711).

* Mon Jul 16 2007 Ian Kent <ikent@redhat.com> - 5.0.2-5
- fix mount point directory creation for bind mounts.
- add quoting for exports gathered by hosts map.

* Mon Jun 25 2007 Ian Kent <ikent@redhat.com> - 5.0.2-4
- update multi map nsswitch patch.

* Mon Jun 25 2007 Ian Kent <ikent@redhat.com> - 5.0.2-3
- add missing "multi" map support.
- add multi map nsswitch lookup.

* Wed Jun 20 2007 Ian Kent <ikent@redhat.com> - 5.0.2-2
- include krb5.h in lookup_ldap.h (some openssl doesn't implicitly include it).
- correct initialization of local var in parse_server_string.

* Mon Jun 18 2007 Ian Kent <ikent@redhat.com> - 5.0.2-1
- Update to upstream release 5.0.2.

* Tue Jun 12 2007 Ian Kent <ikent@redhat.com> - 5.0.1-16
- add ldaps support.
  - note: it's no longer possible to have multiple hosts in an ldap map spec.
  - note: to do this you need to rely on the ldap client config.

* Thu Jun 7 2007 Ian Kent <ikent@redhat.com> - 5.0.1-14
- fix deadlock in alarm manager module.

* Sun Jun 3 2007 Ian Kent <ikent@redhat.com> - 5.0.1-12
- correct mistake in logic test in wildcard lookup.

* Mon May 7 2007 Ian Kent <ikent@redhat.com> - 5.0.1-10
- fix master map lexer to admit "." in macro values.

* Tue Apr 17 2007 Ian Kent <ikent@redhat.com> - 5.0.1-9
- upstream fix for filesystem is local check.
- disable exports access control check (bz 203277).
- fix patch to add command option for set a global mount options (bz 214684).

* Mon Apr 16 2007 Ian Kent <ikent@redhat.com> - 5.0.1-8
- add configuration variable to control appending of global options (bz 214684).
- add command option to set a global mount options string (bz 214684).

* Tue Apr 3 2007 Ian Kent <ikent@redhat.com> - 5.0.1-7
- fix "null" domain netgroup match for "-hosts" map.

* Fri Mar 29 2007 Ian Kent <ikent@redhat.com> - 5.0.1-6
- fix directory creation for browse mounts.
- fix wildcard map handling and improve nsswitch source map update.

* Fri Mar 16 2007 Ian Kent <ikent@redhat.com> - 5.0.1-5
- drop "DEFAULT_" prefix from configuration names.
- add option to select replicated server at random (instead of
  ping response time) (bz 227604).
- fix incorrect cast in directory cleanup routines (bz 231864).

* Thu Mar 8 2007 Ian Kent <ikent@redhat.com> - 5.0.1-4
- fixed numeric export match (bz 231188).

* Thu Mar 1 2007 Ian Kent <ikent@redhat.com> - 5.0.1-3
- change file map lexer to allow white-space only blank lines (bz 229434).

* Fri Feb 23 2007 Ian Kent <ikent@redhat.com> - 5.0.1-2
- update "@network" matching patch.

* Thu Feb 22 2007 Ian Kent <ikent@redhat.com> - 5.0.1-1
- update to release tar.
- fix return check for getpwuid_r and getgrgid_r.
- patch to give up trying to update exports list while host is mounted.
- fix to "@network" matching. 
- patch to check for fstab update and retry if not updated.

* Tue Feb 20 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.24
- add "condrestart" to init script (bz 228860).
- add "@network" and .domain.name export check.
- fix display map name in mount entry for "-hosts" map.

* Fri Feb 16 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.22
- fix localhost replicated mounts not working (bz 208757).

* Wed Feb 14 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.20
- correct return status from do_mkdir (bz 223480).

* Sat Feb 10 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.18
- update the "task done race" patch to fix a deadlock.
- added URL tag.
- removed obsoletes autofs-ldap.
- replaced init directory paths with %%{_initrddir} macro.

* Fri Feb 9 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.17
- make use of spaces and tabs in spec file consistent.
- escape embedded macro text in %%changelog.
- eliminate redundant %%version and %%release.
- remove redundant conditional check from %%clean.
- remove redundant exit from %%preun.
- correct %%defattr spec.
- remove empty %%doc and redundant %%dir misc lines.
- combine program module spec lines into simpler one line form.

* Tue Feb 6 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.15
- fix race when setting task done (bz 227268).

* Mon Jan 29 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.13
- make double quote handing consistent (at least as much as we can).
- fix handling of trailing white space in wildcard lookup (forward port bz 199720).
- check fqdn of each interface when matching export access list (bz 213700).

* Thu Jan 18 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.11
- correct check for busy offset mounts before offset umount (bz 222872).

* Wed Jan 17 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.9
- fix another expire regression introduced in the "mitigate manual umount"
  patch (bz 222872).

* Mon Jan 15 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.7
- ignore "winbind" if it appears in "automount" nsswitch.conf (bz 214632).

* Tue Jan 10 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.5
- remove fullstop from Summary tag.
- change Buildroot to recommended form.
- replace Prereq with Requires.

* Tue Jan 9 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.3
- remove redundant rpath link option (prep for move to Extras).

* Tue Jan 9 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.1
- consolidate to rc3.
- fix typo in Fix typo in var when removing temp directory (bz 221847).

* Wed Dec 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.41
- fix nonstrict multi-mount handling (bz 219383).
- correct detection of duplicate indirect mount entries (bz 220799).

* Thu Dec 14 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.38
- update master map tokenizer to admit "slasify-colons" option.
- update location validation to accept "_" (bz 219445).
- set close-on-exec flag on open sockets (bz 215757).

* Mon Dec 11 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.35
- update "replace-tempnam" patch to create temp files in sane location.

* Mon Dec 11 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.34
- change mount "device" from "automount" to the map name.
- check for buffer overflow in mount_afs.c.
- replace tempnam with mkdtemp.

* Sun Dec 10 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.33
- expand export access checks to include missing syntax options.
- make "-hosts" module try to be sensitive to exports list changes.

* Thu Dec 7 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.32
- remove ability to use multiple indirect mount entries in master
  map (bz 218616).

* Wed Dec 6 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.29
- alter nfs4 host probing to not use portmap lookup and add options
  check for "port=" parameter (bz 208757).
- correct semantics of "-null" map handling (bzs 214800, 208091).

* Sat Nov 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.26
- fix parsing of bad mount mount point in master map (bz 215620).
- fix use after free memory access in cache.c and lookup_yp.c (bz 208091).
- eliminate use of pthread_kill to detect task completion (bz 208091).

* Sun Nov 12 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.23
- fix tokenizer to distinguish between global option and dn string (bz 214684).
- fix incorrect return from spawn.

* Wed Nov 8 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.21
- mitigate manual umount of automounts where possible.
- fix multiply recursive bind mounts.
- check kernel module version and require 5.00 or above.
- fix expire regression introduced in the "mitigate manual umount" patch.
- still more on multiply recursive bind mounts.

* Mon Oct 30 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.20
- Update patch for changed semantics of mkdir in recent kernels.
- fix macro table locking (bz 208091).
- fix nsswitch parser locking (bz 208091).
- allow only one master map read task at a time.
- fix misc memory leaks.

* Wed Oct 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.19
- deal with changed semantics of mkdir in recent kernels.

* Fri Oct 20 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.16
- fix get_query_dn not looking in subtree for LDAP search (missed
  econd occurance).
- allow additional common LDAP attributes in map dn.
- Resolves: rhbz#205997

* Mon Oct 16 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.13
- fix parsing of numeric host names in LDAP map specs (bz 205997).

* Mon Oct 16 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.12
- fix "-fstype=nfs4" server probing (part 2 of bz 208757).
- set close-on-exec flag on open files where possible (bz 207678).

* Fri Oct 13 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.11
- fix file handle leak in nsswitch parser (bz 207678).
- fix memory leak in mount and expire request processing (bz 207678).
- add additional check to prevent running of cancelled tasks.
- fix potential file handle leakage in rpc_subs.c for some failure
  cases (bz 207678).
- fix file handle leak in included map lookup (bz 207678).

* Sat Oct 7 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.10
- fix get_query_dn not looking in subtree for LDAP search.
- allow syntax "--timeout <secs>" for backward compatibility
  (bz 193948).
- make masked_match independent of hostname for exports comparison
  (bz 209638).

* Thu Oct 5 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.9
- fix "-fstype=nfs4" handling (bz 208757).

* Wed Sep 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.8
- review and fix master map options update for map reload.

* Wed Sep 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.7
- make default installed master map for /net use "-hosts" instead
  of auto.net.
- fix included map recursive map key lookup.

* Mon Sep 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.6
- remove unused option UNDERSCORETODOT from default config files.

* Mon Sep 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.5
- fix LDAP lookup delete cache entry only if entry doesn't exist.
- add missing socket close in replicated host check (Jeff Moyer).

* Wed Sep 20 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.4
- fix cache entrys not being cleaned up on submount expire.

* Sun Sep 17 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.3
- fix include check full patch for file map of same name.

* Wed Sep 13 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.2
- fix handling of autofs specific mount options (bz 199777).

* Fri Sep 1 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.1
- consolidate to rc2.
- fix colon escape handling.
- fix recusively referenced bind automounts.
- update kernel patches.

* Fri Aug 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.17
- fix task cancelation at shutdown (more)
- fix concurrent mount and expire race with nested submounts.

* Sun Aug 20 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.16
- fix included map lookup.
- fix directory cleanup on expire.
- fix task cancelation at shutdown.
- fix included map wild card key lookup.

* Thu Aug 16 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.15
- expire individual submounts.
- add ino_index locking.
- fix nested submount expiring away when pwd is base of submount.
- more expire re-work to cope better with shutdown following cthon tests.
- allow hostname to start with numeric when validating.

* Thu Aug 7 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.14
- remove SIGCHLD handler because it is no longer needed and was
  causing expire problems.
- alter expire locking of multi-mounts to lock sub-tree instead of
  entire tree.
- review verbose message feedback and update.
- correction for expire of multi-mounts.
- spelling corrections to release notes (Jeff Moyer).
- add back sloppy mount option, removed for Connectathon testing.
- disable mtab locking again.

* Thu Aug 4 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.13
- tidy up directory cleanup and add validation check to rmdir_path.

* Thu Aug 4 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.12
- enable mtab locking until I can resolve the race with it.

* Thu Aug 4 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.11
- cthon fix expire of wildcard and program mounts broken by recent
  patches.

* Thu Aug 3 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.10
- cthon corrections for shutdown patch below and fix shutdown expire.

* Wed Aug 2 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.9
- cthon fix some shutdown races.

* Thu Jul 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.8
- Fix compile error.

* Thu Jul 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.7
- cthon fix expire of various forms of nested mounts.

* Mon Jul 24 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.6
- cthon more parser corrections and attempt to fix multi-mounts
  with various combinations of submounts (still not right).

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.5
- Add conflicts kernel < 2.6.17.
- Fix submount operation broken by connectathon updates.

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.4
- Correction to host name validation test for connectathon tests.

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.3
- More code cleanup and corrections for connectathon tests.

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.2
- Code cleanup and fixes for connectathon tests.

* Thu Jul 13 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.1
- Update version label to avoid package update problems.

* Thu Jul 13 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-8
- add cacheing of negative lookups to reduce unneeded map
  lookups (bz 197746 part 2).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:5.0.0_beta6-7.1
- rebuild

* Tue Jul 11 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-7
- correct directory cleanup in mount modules.
- merge key and wildcard LDAP query for lookups (bz 197746).

* Sat Jul 8 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-6
- correct test for libhesiod.

* Fri Jul 7 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-5
- correct auto.net installed as auto.smb.
- update LDAP auth - add autodectect option.

* Wed Jul 5 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-4
- correct shutdown log message print.
- correct auth init test when no credentials required.

* Tue Jul 4 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-3
- correct test for existence of auth config file.

* Mon Jul 3 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-2
- merge LDAP authentication update for GSSAPI (Jeff Moyer).
- update default auth config to add options documenetation (Jeff Moyer).
- workaround segfaults at exit after using GSSAPI library.
- fix not checking return in init_ldap_connection (jeff Moyer).

* Thu Jun 29 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-1
- consolidate to beta6, including:
  - mode change update for config file.
  - correction to get_query_dn fix from beta5-4.

* Wed Jun 28 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-6
- cleanup defaults_read_config (Jeff Moyer).

* Tue Jun 27 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-5
- allow global macro defines to override system macros.
- correct spelling error in default config files missed by
  previous update.
- misc correctness and a memory leak fix.

* Mon Jun 26 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-4
- correct spelling error in default config.
- fix default auth config not being installed.
- change LDAP query method as my test db was incorrect.
- change ldap defaults code to handle missing auth config.
- fix mistake in parsing old style LDAP specs.
- update LDAP so that new query method also works for old syntax.

* Fri Jun 23 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-3
- lookup_init cleanup and fix missed memory leak.
- use nis map order to check if update is needed.
- fix couple of memory leaks in lookup_yp.c.
- fix pasre error in replicated server module.

* Wed Jun 21 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-2
- Add openssl-devel to the BuildRequires, as it is needed for the LDAP
  authentication bitsi also.

* Tue Jun 20 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-1
- promote to beta5.

* Tue Jun 20 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-14
- fix directory cleanup at exit.

* Mon Jun 19 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-13
- Change LDAP message severity from crit to degug (bz# 183893).
- Corrections to INSTALL and README.v5.release.
- Add patch to fix segv on overlength map keys in file maps (Jeff Moter).
- Add patch to restrict scanning of /proc to pid directories only (Jeff Moyer).

* Thu Jun 15 2006 Jeff Moyer <jmoyer@redhat.com> - 5.0.0_beta4-12
- Change BuildPrereq to BuildRequires as per the package guidelines.
- Add libxml2-devel to the BuildRequires, as it is needed for the LDAP
  authentication bits.

* Wed Jun 14 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-11
- add export access list matching to "hosts" lookup module (bz # 193585).

* Tue Jun 13 2006 Jeff Moyer <jmoyer@redhat.com> - 5.0.0_beta4-10
- Add a BuildPrereq for cyrus-sasl-devel

* Tue Jun 13 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-9
- move autofs4 module loading back to init script (part bz # 194061).

* Mon Jun 12 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-8
- fix handling of master map entry update (bz # 193718).
- fix program map handling of invalid multi-mount offsets.

* Sat Jun 10 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-7
- fix context init error (introduced by memory leak patch).

* Fri Jun 9 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-6
- add free for working var in get_default_logging.
- add inialisation for kver in autofs_point struct.
- fix sources list corruption in check_update_map_sources.
- fix memory leak in walk_tree.
- fix memory leak in rpc_portmap_getport and rpc_ping_proto.
- fix memory leak in initialisation of lookup modules.

* Wed Jun 8 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-5
- misc fixes for things found while investigating map re-read problem.

* Wed Jun 7 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-4
- check base of offset mount tree is not a mount before umounting
  its offsets.
- fix replicated mount parse for case where last name in list
  fails lookup.
- correct indirect mount expire broken by the wildcard lookup fix.
- fix up multi-mount handling when wildcard map entry present.

* Mon Jun 5 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-3
- correct config names in default.c (jpro@bas.ac.uk).

* Mon Jun 5 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-2
- re-instate v4 directory cleanup (bz# 193832 again).
- backout master map lookup changes made to beta3.
- change default master map from /etc/auto.master to auto.master
  so that we always use nsswitch to locate master map.
- change default installed master map to include "+auto.master"
  to pickup NIS master map (all bz# 193831 again).

* Fri Jun 2 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-1
- update to beta4.
- should address at least bzs 193798, 193770, 193831 and
  possibly 193832.

* Mon May 29 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-6
- add back test for nested mount in program map lookup.
  - I must have commented this out for a reason. I guess we'll
    find out soon enough.

* Mon May 29 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-5
- fix handling of autofs filesystem mount fail on init.

* Sat May 27 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-4
- updated hesiod patch.

* Sat May 27 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-3
- update hesiod module (Jeff Moyer).
  - add mutex to protect against overlapping mount requests.
  - update return from mount request to give more sensible NSS_*
    values.

* Fri May 26 2006 Jeff Moyer <jmoyer@redhat.com> - 1:5.0.0_beta3-2
- Fix the install permissions for auto.master and auto.misc.

* Thu May 25 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-1
- update source to version 5.0.0_beta3.
- add patch to remove extra debug print.
- add patch to
  - fix memory alloc error in nis lookup module.
  - add "_" to "." mapname translation to nis lookup module.
- add patch to add owner pid to mount list struct.
- add patch to disable NFSv4 when probing hosts (at least foe now).
- add patch to fix white space handling in replicated server selection code.
- add patch to prevent striping of debug info macro patch (Jeff Moyer).
- add patch to add sanity checks on rmdir_path and unlink (Jeff Moyer).
- add patch to fix e2fsck error code check (Jeff Moyer).

* Tue May 16 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-23
- add patch to ignore the "bg" and "fg" mount options as they
  aren't relevant for autofs mounts (bz #184386).

* Tue May 2 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-20
- add patch to use "cifs" instead of smbfs and escape speces
  in share names (bz #163999, #187732).

* Tue Apr 11 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-18
- Add patch to allow customization of arguments to the
  autofs-ldap-auto-master program (bz #187525).
- Add patch to escap "#" characters in exports from auto.net
  program mount (bz#178304).

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:4.1.4-16.2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:4.1.4-16.2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Feb 1 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-16.2
- Add more general patch to translate "_" to "." in map names. (bz #147765)

* Mon Jan 25 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-16.1
- Add patch to use LDAP_DEPRICATED compile option. (bz #173833)

* Mon Jan 17 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-16
- Replace check-is-multi with more general multi-parse-fix.
- Add fix for premature return when waiting for lock file.
- Update copyright declaration for reentrant-syslog source.
- Add patch for configure option to disable locking during mount.
  But don't disable locking by default.
- Add ability to handle automount schema used in Sun directory server.
- Quell compiler warning about getsockopt parameter.
- Quell compiler warning about yp_order parameter.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 17 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-14
- Removed the /misc entry from the default auto.master.  auto.misc has
  an entry for the cdrom device, and the preferred method of mounting the
  cd is via udev/hal.

* Mon Nov  7 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-13
- Changed to sort -k 1, since that should be the same as +0.

* Thu Nov  3 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-12
- The sort command no longer accepts options of the form "+0".  This broke
  auto.net, so the option was removed.  Fixes bz #172111.

* Wed Oct 26 2005  <jmoyer@redhat.com> - 1:4.1.4-11
- Check the return code of is_local_addr in get_best_mount. (bz #169523)

* Wed Oct 26 2005  <jmoyer@redhat.com> - 1:4.1.4-10
- Fix some bugs in the parser
- allow -net instead of /etc/auto.net
- Fix a buffer overflow with large key lengths
- Don't allow autofs to unlink files, only to remove directories
- change to the upstream reentrant syslog patch from the band-aid deferred
  syslog patch.
- Get rid of the init script patch that hard-coded the release to redhat.
  This should be handled properly by all red hat distros.

* Wed May  4 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-8
- Add in the deferred syslog patch.  This fixes a hung automounter issue
  related to unsafe calls to syslog in signal handler context.

* Tue May  3 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-7
- I reversed the checking for multimount entries, breaking those configs!
  This update puts the code back the way it was before I broke it.

* Tue Apr 26 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-6
- Fix a race between mounting a share and updating the cache in the parent
  process.  If the mount completed first, the parent would not expire the
  stale entry, leaving it first on the list.  This causes map updates to not
  be recognized (well, worse, they are recognized after the first expire, but
  not subsequent ones).  Fixes a regression, bug #137026 (rhel3 bug).

* Fri Apr 15 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.4-5
- Fixed regression with -browse not taking effect.

* Wed Apr 13 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-4
- Finish up with the merge breakage.
- Temporary fix for the multimount detection code.  It seems half-baked.

* Wed Apr 13 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-3
- Fix up the one-auto-master patch.  My "improvements" had side-effects.

* Wed Apr 13 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-2
- Import 4.1.4 and merge.

* Mon Apr  4 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-123
- Add in an error case that was omitted in the multi-over patch.
- Update our auto.net to reflect the changes that went into 4.1.4_beta2.
  This fixes a problem seen by at least one customer where a malformed entry
  appeared first in the multimount list, thus causing the entire multimount
  to be ignored.  This new auto.net places that entry at the end, purely by
  luck, but it fixes the problem in this one case.

* Thu Mar 31 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-119
- Merge in the multi-over patch.  This resolves an issue whereby multimounts
  (such as those used for /net) could be processed in the wrong order,
  resulting in directories not showing up in a multimount tree.  The fix
  is to process these directories in order, shortest to longer path.

* Wed Mar 23 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-115
- Fixed regression causing any entries after a wildcard in an
  indirect map to be ignored. (bz #151668).
- Fixed regression which caused local hosts to be mount instead
  of --bind local directories. (bz #146887)

* Thu Mar 17 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-111
- Fixed one off bug in the submount-variable-propagation patch.
  (bz #143074)
- Fixed a bug in the init script which wouldn't find the -browse
  option if it was preceded by another option. (fz #113494)

* Mon Feb 28 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-100
- When using ldap if auto.master doesn't exist we now check for auto_master.
  Addresses bz #130079
- When using an auto.smb map we now remove the leading ':' from the path which
  caused mount to fail in the past.  Addresses bz #147492
- Autofs now checks /etc/nsswitch.conf to determine in what order files & nis
  are checked when looking up autofs submount maps which don't specify a
  maptype.  Addresses IT #57612.

* Mon Feb 14 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-99
- Change Copyright to License in the spec file so it will build.

* Fri Feb 11 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-98
- Program maps can repeat the last character of output.  Fix this.  
  Addresses bz #138606
- Return first entry when there are duplicate keys in a map.  Addresses
  bz #140108.
- Propagate custom map variables to submounts.  Fixes bz #143074.
- Create a sysconfig variable to control whether we source only one master
  map (the way sun does), or source all maps found (which is the default for
  backwards compatibility).  Addresses bz #143126.
- Revised version of the get_best_mount patch. (#146887) cfeist@redhat.com
  The previous patch introduced a regression.  Non-replicated mounts would
  not have the white space stripped from the entry and the mount would fail.
- Handle comment characters in the middle of the automount line in
  /etc/nsswitch.conf.  Addresses bz #127457.

* Wed Feb  2 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-94
- Stop automount from pinging hosts if there is only one host (#146887)

* Wed Feb  2 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-90
- Fix potential double free in cache_release.  This bug showed up in a
  multi-map setup.  Two calls to cache_release would result in a SIGSEGV,
  and the automount process would never exit.

* Mon Jan 24 2005 Chris Feist <cfeist@redhat.com> - 1:4.3-82
- Fixed documentation so users know that any local mounts override
  any other weighted mount.

* Mon Jan 24 2005 Chris Feist <cfeist@redhat.com> - 1:4.3-80
- Added a variable to determine if we created the directory or not
  so we don't accidently remove a directory that we didn't create when
  we stop autofs.  (bz #134399)

* Tue Jan 11 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-76
- Fix the large program map patch.

* Tue Jan 11 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-75
- Fix some merging breakages that caused the package not to build.

* Thu Jan  6 2005  <jmoyer@redhat.com> - 1:4.1.3-74
- Add in the map expiry patch
- Bring in other patches that have been committed to other branches. This 
  version should now contain all fixes we have to date
- Merge conflicts due to map expiry changes

* Fri Nov 19 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-57
- Pass a socket into clntudp_bufcreate so that we don't use up additional 
  reserved ports.  This patch, along with the socket leak fix, addresses
  bz #128966.

* Wed Nov 17 2004  <jmoyer@redhat.com> - 1:4.1.3-56
- Somehow the -browse patch either didn't get committed or got reverted.
  Fixed.

* Tue Nov 16 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-55
- Fix program maps so that they can have gt 4k characters. (Neil Horman)
  Addresses bz #138994.
- Add a space after the colon here "Starting automounter:" in init script.
  Fixes bz #138513.

* Mon Nov 15 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-53
- Make autofs understand -[no]browse.  Addresses fz #113494.

* Thu Nov 11 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-48
- Fix the umount loop device function in the init script.

* Wed Oct 27 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-34
- Added a patch to fix the automounter failing on ldap maps
  when it couldn't get the whole map.  (ie. when the search
  limit was lower than the number of results)

* Thu Oct 21 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-32
- Fixed the use of +ypmapname so the maps included with +ypmapname
  are used in the correct order.  (In the past the '+' entries
  were always processed after local entries.)

* Thu Oct 21 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-31
- Fixed the duplicate map detection code to detect if maps try
  to mount on top of existing maps. 

* Wed Oct 20 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-29
- Fixed a problem with backwards compatability. Specifying local
  maps without '/etc/' prepended to them now works. (bz #136038)

* Fri Oct 15 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-28
- Fixed a bug which caused directories to never be unmounted. (bz #134403)

* Thu Oct 14 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-27
- Fixed an error in the init script which caused duplicate entries to be
  displayed when asking for autofs status.

* Fri Oct  1 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-22
- Comment out map expiry (and related) patch for an FC3 build.

* Thu Sep 23 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-21
- Make local options apply to all maps in a multi-map entry.

* Tue Sep 21 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-20
- Merged my and Ian's socket leak fixes into one, smaller patch. Only
  partially addresses bz #128966.
- Fix some more echo lines for internationalization. bz #77820
- Revert the only one auto.master patch until we implement the +auto_master
  syntax.  Temporarily addresses bz #133055.

* Thu Sep  2 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-18
- Umount loopback filesystems under automount points when stopping the 
  automounter.
- Uncomment the map expiry patch.
- change a close to an fclose in lookup_file.c

* Tue Aug 31 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-17
- Add patch to support parsing nsswitch.conf to determine map sources.
- Disable this patch, and Ian's map expiry patch for a FC build.

* Tue Aug 24 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-16
- Version 3 of Ian's map expiry changes.

* Wed Aug 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-15
- Fix a socket leak in the rpc_subs, causing mounts to fail since we are 
  running out of port space fairly quickly.

* Wed Aug 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-14
- New map expiry patch from Ian.
- Fix a couple signal races.  No known problem reports of these, but they
  are holes, none-the-less.

* Tue Aug 10 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-13
- Only read one auto.master map (instead of concatenating all found sources).
- Uncomment Ian's experimental mount expiry patch.

* Fri Aug  6 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-12
- Add a sysconfig entry to disable direct map support, and set this to 
  1 by default.
- Disable the beta map expiry logic so I can build into a stable distro.
- Add defaults for all of the sysconfig variables to the init script so 
  we don't trip over user errors (i.e. deleting /etc/sysconfig/autofs).

* Wed Aug  4 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-11
- Add beta map expiry code for wider testing. (Ian Kent)
- Fix check for ghosting option.  I forgot to check for it in DAEMONOPTIONS.
- Remove STRIPDASH from /etc/sysconfig/autofs

* Mon Jul 12 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-10
- Add bad chdir patch from Ian Kent.
- Add a typo fix for the mtab lock file.
- Nuke the stripdash patch.  It didn't solve a problem.

* Tue Jun 22 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-9
- Bump revison for inclusion in RHEL 3.

* Mon Jun 21 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-8
- Change icmp ping to an rpc ping.  (Ian Kent)
- Fix i18n patch
  o Remove the extra \" from one echo line.
  o Use echo -e if we are going to do a \n in the echo string.

* Mon Jun 21 2004 Alan Cox <alan@redhat.com>
- Fixed i18n bug #107463

* Mon Jun 21 2004 Alan Cox <alan@redhat.com>
- Fixed i18n bug #107461

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Jun  5 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-4
- Perform an icmp ping request before rpc_pings, since the rpc clnt_create
  function has a builtin default timeout of 60 seconds.  This could result
  in a long delay when a server in a replicated mount setup is down.
- For non-replicated server entries, ping a host before attempting to mount.
  (Ian Kent)
- Change to %%configure.
- Put version-release into .version to allow for automount --version to
  print exact info.
- Nuke my get-best-mount patch which always uses the long timeout.  This
  should no longer be needed.
- Put name into changelog entries to make them consistent.  Add e:n-v-r
  into Florian's entry.
- Stop autofs before uninstalling

* Sat Jun 05 2004 Florian La Roche <Florian.LaRoche@redhat.de> - 1:4.1.3-3
- add a preun script to remove autofs

* Tue Jun  1 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-2
- Incorporate patch from Ian which fixes an infinite loop seen by those
  running older versions of the kernel patches (triggered by non-strict mounts
  being the default).

* Tue Jun  1 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-1
- Update to upstream 4.1.3.

* Thu May  6 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-6
- The lookup_yp module only dealt with YPERR_KEY, all other errors were 
  treated as success.  As a result, if the ypdomain was not bound, the 
  subprocess that starts mounts would SIGSEGV.  This is now fixed.
- Option parsing in the init script was not precise enough, sometimes matching
  filesystem options to one of --ghost, --timeout, --verbose, or --debug.  
  The option-parsing patch addresses this issue by making the regexp's much
  more precise.
- Ian has rolled a third version of the replicated mount fixes.

* Tue May  4 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-5
- Ian has a new fix for replicated server and multi-mounts.  Updated the 
  patch for testing.  Still beta.  (Ian Kent)

* Mon May  3 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-4
- Fix broken multi-mounts.  test patch.  (Ian Kent)

* Tue Apr 20 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-3
- Fix a call to spawnl which forgot to specify a lock file. (nphilipp)

* Wed Apr 14 2004  <jmoyer@redhat.com> - 1:4.1.2-2
- Pass --libdir= to ./configure so we get this right on 64 bit platforms that 
  support backwards compat.

* Wed Apr 14 2004  Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-1
- Change hard-coded paths in the spec file to the %%{_xxx} variety.
- Update to upstream 4.1.2.
- Add a STRIPDASH option to /etc/sysconfig/autofs which allows for
  compatibility with the Sun automounter options specification syntax in
  auto.master.  See /etc/sysconfig/autofs for more information.  Addresses
  bug 113950.

* Tue Apr  6 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-6
- Add the /etc/sysconfig/autofs file, and supporting infrastructure in 
  the init script.
- Add support for UNDERSCORE_TO_DOT for those who want it.
- We no longer own /net.  Move it to the filesystem package.

* Tue Mar 30 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-5
- Clarify documentation on direct maps.
- Send automount daemons a HUP signal during reload.  This tells them to 
  re-read maps (otherwise they use a cached version.  Patch from the autofs
  maintainer.

* Mon Mar 22 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-4
- Fix init script to print out failures where appropriate.
- Build the automount daemon as a PIE.

* Thu Mar 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-3
- Fix bug in get_best_mount, whereby if there is only one option, we 
  choose nothing.  This is primarily due to the fact that we pass 0 in to
  the get_best_mount function for the long timeout parameter.  So, we
  timeout trying to contact our first and only server, and never retry.

* Thu Mar 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-2
- Prevent startup if a mountpoint is already mounted.

* Thu Mar 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-1
- Update to 4.1.1, as it fixes problems with wildcards that people are 
  seeing quite a bit.

* Wed Mar 17 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.0-8
- Fix ldap init code to parse server name and options correctly.

* Tue Mar 16 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.0-7
- Moved the freeing of ap.path to cleanup_exit, as we would otherwise 
  reference an already-freed variable.

* Mon Mar 15 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.0-6
- add %%config(noreplace) for auto.* config files.

* Wed Mar 10 2004 Jeff Moyer <jmoyer@redhat.com> 1:4.1.0-5
- make the init script only recognize redhat systems.  Nalin seems to remember
  some arcane build system error that can be caused if we don't do this.

* Wed Mar 10 2004 Jeff Moyer <jmoyer@redhat.com> 1:4.1.0-4
- comment out /net and /misc from the default auto.master.  /net is important
  since in a default shipping install, we can neatly co-exist with amd.

* Wed Mar 10 2004 Jeff Moyer <jmoyer@redhat.com> 1:4.1.0-3
- Ported forward Red Hat's patches from 3.1.7 that were not already present
  in 4.1.0.
- Moving autofs from version 3.1.7 to 4.1.0

* Mon Sep 29 2003 Ian Kent <raven@themaw.net>
- Added work around for O(1) patch oddity.

* Sat Aug 17 2003 Ian Kent <raven@themaw.net>
- Fixed tree mounts.
- Corrected transciption error in autofs4-2.4.18 kernel module

* Sun Aug 10 2003 Ian Kent <raven@themaw.net>
- Checked and merged most of the RedHat v3 patches
- Fixed kernel module handling wu-ftpd login problem (again)

* Thu Aug 7 2003 Ian Kent <raven@themaw.net>
- Removed ineffective lock stuff
- Added -n to bind mount to prevent mtab update error
- Added retry to autofs umount to clean matb after fail
- Redirected messages from above to debug log and added info message
- Fixed autofs4 module reentrancy, pwd and chroot handling

* Wed Jul 30 2003 Ian Kent <raven@themaw.net>
- Fixed autofs4 ghosting patch for 2.4.19 and above (again)
- Fixed autofs directory removal on failure of autofs mount
- Fixed lock file wait function overlapping calls to (u)mount

* Sun Jul 27 2003 Ian Kent <raven@themaw.net>
- Implemented LDAP direct map handling for nisMap and automountMap schema
- Fixed autofs4 ghosting patch for 2.4.19 and above (again)
- Added locking to fix overlapping internal calls to (u)mount 
- Added wait for mtab~ to improve tolerance of overlapping external calls to (u)mount
- Fixed ghosted directory removal after failed mount attempt

* Wed May 28 2003 Ian Kent <raven@themaw.net>
- Cleaned up an restructured my added code
- Corrected ghosting problem with 2.4.19 and above
- Added autofs4 ghosting patch for 2.4.19 and above
- Implemented HUP signal to force update of ghosted maps

* Mon Mar 23 2002 Ian Kent <ian.kent@pobox.com>
- Add patch to implement directory ghosting and direct mounts
- Add patch to for autofs4 module to support ghosting

* Wed Jan 17 2001 Nalin Dahyabhai <nalin@redhat.com>
- use -fPIC instead of -fpic for modules and honor other RPM_OPT_FLAGS

* Tue Feb 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- enable hesiod support over libbind

* Fri Aug 13 1999 Cristian Gafton <gafton@redhat.com>
- add patch from rth to avoid an infinite loop
