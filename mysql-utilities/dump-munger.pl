#!/usr/bin/perl -w

#
# dump-munger.pl
# Copyright (C) 2011, 2015, After6 Services LLC.  All Rights Reserved.
#
# This script was created to cut down on the size of restored production databases that need
# to be worked with for testing and development purposes.
#
# Basically, we filter the comments, entries, log, and trackback entries.
#

$|++;

open ORIGINAL, "<", "original-database.sql" || die "Open ORIGINAL faield with: $!\n";
open REVISED, ">", "munged.sql" || die "Open REVISED failed with: $!\n";

while ($line = <ORIGINAL>) {
    print REVISED $line if ($line !~ /^INSERT INTO `mt_(comment|entry|log|tbping|trackback)/)
}

close ORIGINAL;
close REVISED;
