#!/usr/bin/perl -w
# Change above line to path to your perl binary
#
# GD-test.cgi
# by Dave Aiello
# Copyright (C) 2012, After6 Services LLC. All Rights Reserved.
#
# The code snippet used in the test was published in the article
# "Exploring Perl Modules - Part 1: On-The-Fly Graphics with GD" by
# Pradeep Padala, Linux Gazette, August 2002,
# http://linuxgazette.net/issue81/padala.html 

# Load the perl modules that the script needs to perform its work.  Also
# load perl modules that will provide the greatest possible output if there
# are errors, so that further troubleshooting can be done.
#
use strict;
use warnings;
use GD;

# Generate the Content-type necessary to tell the browser to render what
# we're about to create as an image.
print "Content-type: image/gif\r\n\r\n";

# Make sure we are writing to a binary stream
binmode STDOUT;

# Create a new image
my $im = new GD::Image(100,100);

# Allocate some colors
my $white = $im->colorAllocate(255,255,255);
my $black = $im->colorAllocate(0,0,0);
my $red = $im->colorAllocate(255,0,0);
my $blue = $im->colorAllocate(0,0,255);

# Make the background transparent and interlaced
$im->transparent($white);
$im->interlaced('true');

# Put a black frame around the picture
$im->rectangle(0,0,99,99,$black);

# Draw a blue oval
$im->arc(50,50,95,75,0,360,$blue);

# And fill it with red
$im->fill(50,50,$red);

# Convert the image to PNG and print it to the STDOUT
print $im->png;

# Tell perl to exit the script.
exit;
