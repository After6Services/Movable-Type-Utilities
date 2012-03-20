#!/usr/bin/perl -w
# Change above line to path to your perl binary
#
# image-magick-test.cgi
# by Dave Aiello
# Copyright (C) 2011-2012, After6 Services LLC.  All Rights Reserved.
#
# Make simple beveled button and output to STDOUT in GIF format
#
# to embed this image in a web page, use:
# img src="/cgi-bin/image-magick-test.cgi"
#

use strict;
use warnings;
use Image::Magick;

# Generate the Content-type necessary to tell the browser to render what
# we're about to create as an image.
print "Content-type: image/gif\r\n\r\n";

# Instantiate ImageMagick and create a new image.
my $image=Image::Magick->new;

# Set the size to 30 x 180.
$image->Set(size=>'30x180');

# Create a color gradient. Then do a few transformations on it.
$image->Read("gradient:#ff0000-#0000ff");
$image->Raise('3x3');
$image->Rotate(-90);

# Make sure we are writing to a binary stream and write out the image.
binmode STDOUT;
$image->Write('gif:-');

# Tell perl to exit the script.
exit;
