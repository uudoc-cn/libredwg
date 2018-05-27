/* -*- c -*- */
/*****************************************************************************/
/*  LibreDWG - free implementation of the DWG file format                    */
/*                                                                           */
/*  Copyright (C) 2018 Free Software Foundation, Inc.                        */
/*                                                                           */
/*  This library is free software, licensed under the terms of the GNU       */
/*  General Public License as published by the Free Software Foundation,     */
/*  either version 3 of the License, or (at your option) any later version.  */
/*  You should have received a copy of the GNU General Public License        */
/*  along with this program.  If not, see <http://www.gnu.org/licenses/>.    */
/*****************************************************************************/

/*
 * header_variables_dxf.spec: DXF header variables specification
 * written by Reini Urban
 */

//TODO: SINCE(R_2010): LASTSAVEDBY, 1, ""

#include "spec.h"

  SECTION(HEADER);

  HEADER_VALUE (ACADVER, TV, 1, version_codes[dwg->header.version]);

  if (minimal) {
    HEADER_VALUE (HANDSEED, RS, 5, _obj->HANDSEED->absolute_ref);
    ENDSEC();
    return;
  }

  SINCE(R_13) {
    HEADER_VALUE (ACADMAINTVER, RC, 70, dwg->header.maint_version);
  }
  SINCE(R_10) {
    HEADER_VALUE (DWGCODEPAGE, TV, 3, codepage);
  }
  SINCE(R_2010) {
    HEADER_VALUE (LASTSAVEDBY, TV, 1, ""); //TODO
  }
  SINCE(R_2013) {
    HEADER_BLL (REQUIREDVERSIONS, 160);
  }
  HEADER_3D (INSBASE);
  HEADER_3D (EXTMIN);
  HEADER_3D (EXTMAX);
  HEADER_2D (LIMMIN);
  HEADER_2D (LIMMAX);

  HEADER_RC (ORTHOMODE, 70);
  HEADER_RC (REGENMODE, 70);
  HEADER_RC (FILLMODE, 70);
  HEADER_RC (QTEXTMODE, 70);
  HEADER_RC (MIRRTEXT, 70);
  UNTIL(R_14) {
    HEADER_RC (DRAGMODE, 70);
  }
  HEADER_RD (LTSCALE, 40);
  UNTIL(R_14) {
    HEADER_RC (OSMODE, 70);
  }
  HEADER_RC (ATTMODE, 70);
  HEADER_RD (TEXTSIZE, 40);
  HEADER_RD (TRACEWID, 40);

  HEADER_HANDLE_NAME (TEXTSTYLE, 7, STYLE);
  HEADER_HANDLE_NAME (CLAYER, 8, LAYER);
  HEADER_HANDLE_NAME (CELTYPE, 6, LTYPE);
  HEADER_CMC (CECOLOR, 62);
  SINCE(R_13) {
    HEADER_RD (CELTSCALE, 40);
    UNTIL(R_14) {
      HEADER_RC (DELOBJ, 70);
    }
    HEADER_RC (DISPSILH, 70); // this is WIREFRAME
    HEADER_RD (DIMSCALE, 40);
  }
  HEADER_RD (DIMASZ, 40);
  HEADER_RD (DIMEXO, 40);
  HEADER_RD (DIMDLI, 40);
  HEADER_RD (DIMRND, 40);
  HEADER_RD (DIMDLE, 40);
  HEADER_RD (DIMEXE, 40);
  HEADER_RD (DIMTP, 40);
  HEADER_RD (DIMTM, 40);
  HEADER_RD (DIMTXT, 40);
  HEADER_RD (DIMCEN, 40);
  HEADER_RD (DIMTSZ, 40);
  HEADER_RC (DIMTOL, 70);
  HEADER_RC (DIMLIM, 70);
  HEADER_RC (DIMTIH, 70);
  HEADER_RC (DIMTOH, 70);
  HEADER_RC (DIMSE1, 70);
  HEADER_RC (DIMSE2, 70);
  HEADER_RC (DIMTAD, 70);
  HEADER_RC (DIMZIN, 70);
  HEADER_HANDLE_NAME (DIMBLK, 1, BLOCK_HEADER);
  HEADER_RC (DIMASO, 70);
  HEADER_RC (DIMSHO, 70);
  VERSIONS(R_13, R_14) {
    HEADER_RC (DIMSAV, 70); //?
  }
  HEADER_TV (DIMPOST, 1);
  HEADER_TV (DIMAPOST, 1);
  HEADER_RC (DIMALT, 70);
  HEADER_RC (DIMALTD, 70);
  HEADER_RD (DIMALTF, 40);
  HEADER_RD (DIMLFAC, 40);
  HEADER_RC (DIMTOFL, 70);
  HEADER_RD (DIMTVP, 40);
  HEADER_RC (DIMTIX, 70);
  HEADER_RC (DIMSOXD, 70);
  HEADER_RC (DIMSAH, 70);
  HEADER_HANDLE_NAME (DIMBLK1, 1,  BLOCK_HEADER);
  HEADER_HANDLE_NAME (DIMBLK2, 1,  BLOCK_HEADER);
  HEADER_HANDLE_NAME (DIMSTYLE, 2, DIMSTYLE);
  HEADER_CMC (DIMCLRD, 70);
  HEADER_CMC (DIMCLRE, 70);
  HEADER_CMC (DIMCLRT, 70);
  HEADER_RD (DIMTFAC, 40);
  HEADER_RD (DIMGAP, 40);
  SINCE(R_13) {
    HEADER_RC (DIMJUST, 70);
    HEADER_RC (DIMSD1, 70);
    HEADER_RC (DIMSD2, 70);
    HEADER_RC (DIMTOLJ, 70);
    HEADER_RC (DIMTZIN, 70);
    HEADER_RC (DIMALTZ, 70);
    HEADER_RC (DIMALTTZ, 70);
    HEADER_RC (DIMFIT, 70);  //optional
    HEADER_RC (DIMUPT, 70);
    HEADER_RC (DIMUNIT, 70); //optional
    HEADER_RC (DIMDEC, 70);
    HEADER_RC (DIMTDEC, 70);
    HEADER_RC (DIMALTU, 70);
    HEADER_RC (DIMALTTD, 70);
    HEADER_HANDLE_NAME (DIMTXSTY, 7, STYLE);
    HEADER_RC (DIMAUNIT, 70);
  }
  SINCE(R_2000) {
    HEADER_RC (DIMADEC, 70);
    HEADER_RD (DIMALTRND, 40);
    HEADER_RC (DIMAZIN, 70);
    HEADER_RC (DIMDSEP, 70);
    HEADER_RC (DIMATFIT, 70);
    HEADER_RC (DIMFRAC, 70);
    HEADER_HANDLE_NAME (DIMLDRBLK, 1, BLOCK_HEADER);
    HEADER_RC (DIMLUNIT, 70);
    //HEADER_RC (DIMLWD, 70); convert from unsigned to signed
    //HEADER_RC (DIMLWE, 70);
    HEADER_VALUE (DIMLWD, RS, 70, (int16_t)_obj->DIMLWD);
    HEADER_VALUE (DIMLWE, RS, 70, (int16_t)_obj->DIMLWE);
    HEADER_RC (DIMTMOVE, 70);
  }
  HEADER_RC (LUNITS, 70);
  HEADER_RC (LUPREC, 70);
  HEADER_RD (SKETCHINC, 40);
  HEADER_RD (FILLETRAD, 40);
  HEADER_RC (AUNITS, 70);
  HEADER_RC (AUPREC, 70);
  HEADER_TV (MENU, 1);
  HEADER_RD (ELEVATION, 40);
  HEADER_RD (PELEVATION, 40);
  HEADER_RD (THICKNESS, 40);
  HEADER_RC (LIMCHECK, 70);
  UNTIL(R_14) {
    //HEADER_RC (BLIPMODE, 70); //documented but nowhere found
  }
  HEADER_RD (CHAMFERA, 40);
  HEADER_RD (CHAMFERB, 40);
  SINCE(R_13) {
    HEADER_RD (CHAMFERC, 40);
    HEADER_RD (CHAMFERD, 40);
  }
  HEADER_RC (SKPOLY, 70);

  ms = (double)_obj->TDCREATE.ms;
  HEADER_VALUE (TDCREATE, RD, 40, _obj->TDCREATE.days + ms);
  SINCE(R_13) {
    HEADER_VALUE (TDUCREATE, RD, 40, _obj->TDCREATE.days + ms);
  }
  ms = (double)_obj->TDUPDATE.ms;
  HEADER_VALUE (TDUPDATE, RD, 40, _obj->TDUPDATE.days + ms);
  SINCE(R_13) { //TODO decode properly
    ms = (double)_obj->TDUPDATE.ms;
    HEADER_VALUE (TDUUPDATE, RD, 40, _obj->TDUPDATE.days + ms);
  }
  ms = (double)dwg->header_vars.TDINDWG.ms;
  HEADER_VALUE (TDINDWG, RD, 40, dwg->header_vars.TDINDWG.days + ms);
  ms = (double)dwg->header_vars.TDUSRTIMER.ms;
  HEADER_VALUE (TDUSRTIMER, RD, 40, dwg->header_vars.TDUSRTIMER.days + ms);

  HEADER_VALUE (USRTIMER, RC, 70, 1); // 1
  HEADER_RD (ANGBASE, 50);
  HEADER_RC (ANGDIR, 70);
  HEADER_RC (PDMODE, 70);
  HEADER_RD (PDSIZE, 40);
  HEADER_RD (PLINEWID, 40);
  UNTIL(R_14) {
    HEADER_RC (COORDS, 70); // 2
  }
  HEADER_RC (SPLFRAME, 70);
  HEADER_RC (SPLINETYPE, 70);
  HEADER_RC (SPLINESEGS, 70);
  UNTIL(R_14) {
    HEADER_RC (ATTDIA, 70); //default 1
    HEADER_RC (ATTREQ, 70); //default 1
    HEADER_RC (HANDLING, 70); //default 1
  }

  HEADER_VALUE (HANDSEED, RS, 5, _obj->HANDSEED->absolute_ref); 
  //HEADER_H (HANDSEED, 5); //default: 20000, before r13: 0xB8BC

  HEADER_RC (SURFTAB1, 70); // 6
  HEADER_RC (SURFTAB2, 70); // 6
  HEADER_RC (SURFTYPE, 70); // 6
  HEADER_RC (SURFU, 70); // 6
  HEADER_RC (SURFV, 70); // 6
  SINCE(R_2000) {
    HEADER_HANDLE_NAME (UCSBASE, 2, UCS);
  }
  HEADER_HANDLE_NAME (UCSNAME, 2, UCS);
  HEADER_3D (UCSORG);
  HEADER_3D (UCSXDIR);
  HEADER_3D (UCSYDIR);
  SINCE(R_2000) {
    HEADER_HANDLE_NAME (UCSORTHOREF, 2, UCS);
    HEADER_RC (UCSORTHOVIEW, 70);
    HEADER_3D (UCSORGTOP);
    HEADER_3D (UCSORGBOTTOM);
    HEADER_3D (UCSORGLEFT);
    HEADER_3D (UCSORGRIGHT);
    HEADER_3D (UCSORGFRONT);
    HEADER_3D (UCSORGBACK);
    HEADER_HANDLE_NAME (PUCSBASE, 2, UCS);
  }
  HEADER_HANDLE_NAME (PUCSNAME, 2, UCS);
  HEADER_3D (PUCSORG);
  HEADER_3D (PUCSXDIR);
  HEADER_3D (PUCSYDIR);
  SINCE(R_2000) {
    HEADER_HANDLE_NAME (PUCSORTHOREF, 2, UCS);
    HEADER_RC (PUCSORTHOVIEW, 70);
    HEADER_3D (PUCSORGTOP);
    HEADER_3D (PUCSORGBOTTOM);
    HEADER_3D (PUCSORGLEFT);
    HEADER_3D (PUCSORGRIGHT);
    HEADER_3D (PUCSORGFRONT);
    HEADER_3D (PUCSORGBACK);
  }

  HEADER_RC (USERI1, 70);
  HEADER_RC (USERI2, 70);
  HEADER_RC (USERI3, 70);
  HEADER_RC (USERI4, 70);
  HEADER_RC (USERI5, 70);
  HEADER_RD (USERR1, 40);
  HEADER_RD (USERR2, 40);
  HEADER_RD (USERR3, 40);
  HEADER_RD (USERR4, 40);
  HEADER_RD (USERR5, 40);

  HEADER_RC (WORLDVIEW, 70);
  //VERSION(R_13) {
  //  HEADER_RC (WIREFRAME, 70); //Undocumented
  //}
  HEADER_RC (SHADEDGE, 70);
  HEADER_RC (SHADEDIF, 70);
  HEADER_RC (TILEMODE, 70);
  HEADER_RC (MAXACTVP, 70);

  HEADER_3D (PINSBASE);
  HEADER_RC (PLIMCHECK, 70);
  HEADER_3D (PEXTMIN);
  HEADER_3D (PEXTMAX);
  HEADER_2D (PLIMMIN);
  HEADER_2D (PLIMMAX);

  HEADER_RC (UNITMODE, 70);
  HEADER_RC (VISRETAIN, 70);
  VERSION(R_13) {
    HEADER_RC (DELOBJ, 70);
  }
  HEADER_RC (PLINEGEN, 70);
  HEADER_RC (PSLTSCALE, 70);
  HEADER_RC (TREEDEPTH, 70);
  UNTIL(R_11) {
    HEADER_VALUE (DWGCODEPAGE, TV, 3, codepage);
  }
  VERSIONS(R_14, R_2000) { //? maybe only for r14
    HEADER_RC (PICKSTYLE, 70);
  }
  HEADER_HANDLE_NAME (CMLSTYLE, 2, MLINESTYLE); //default: Standard
  HEADER_RC (CMLJUST, 70);
  HEADER_RD (CMLSCALE, 40); //default: 20
  VERSION(R_13) {
    HEADER_RC (SAVEIMAGES, 70);
  }
  SINCE(R_14) {
    HEADER_RC (PROXYGRAPHICS, 70);
  }
  HEADER_VALUE (MEASUREMENT, RC, 70,
                dwg->header.num_sections > SECTION_MEASUREMENT_R13 ? 1 : 0);
  SINCE(R_2000) {
    HEADER_RC (CELWEIGHT, 370);
    HEADER_RC (ENDCAPS, 280);
    HEADER_RC (JOINSTYLE, 280);
    HEADER_RC (LWDISPLAY, 290);
    HEADER_RC (INSUNITS, 70);
    HEADER_TV (HYPERLINKBASE, 1);
    HEADER_TV (STYLESHEET, 1);
    HEADER_RC (XEDIT, 290);
    HEADER_RC (CEPSNTYPE, 380);

    if (dwg->header_vars.CEPSNTYPE == 3)
    {
      HEADER_HANDLE_NAME (CPSNID, 390, LTYPE);
    }
    HEADER_RC (PSTYLEMODE, 290);
    HEADER_TV (FINGERPRINTGUID, 2);
    HEADER_TV (VERSIONGUID, 2);
    HEADER_RC (EXTNAMES, 290);
    HEADER_RD (PSVPSCALE, 40);
    HEADER_RC (OLESTARTUP, 290);
  }

  ENDSEC();

