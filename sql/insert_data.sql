insert into
categories (name)
values
  ('cake'),
  ('cookie'),
  ('tart');

insert into
types (name)
values
  ('product'),
  ('card');

insert into
products (name, main_image, images, description, short_description, price, weight, dimensions, category_id)
values
  ('Matcha Cake',
   'https://i.imgur.com/e4M83hV.jpeg',
   array ['https://i.imgur.com/e4M83hV.jpeg',
    'https://i.imgur.com/cwWsTB4.jpeg',
    'https://i.imgur.com/PST0HJj.jpeg',
    'https://i.imgur.com/r1cVT3W.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    150.00, '230g', '50 x 50 x 10cm', 1),
  ('CARROT CAKE',
   'https://i.imgur.com/UpSPeDB.jpeg',
   array ['https://i.imgur.com/UpSPeDB.jpeg',
    'https://i.imgur.com/VufJfIf.jpeg',
    'https://i.imgur.com/1Vof5hK.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    50.00, '230g', '50 x 50 x 10cm', 1),
  ('Mimosa',
   'https://i.imgur.com/wIvz3fM.jpeg',
   array ['https://i.imgur.com/wIvz3fM.jpeg',
    'https://i.imgur.com/pqFuxEr.jpeg',
    'https://i.imgur.com/7DllORn.jpeg',
    'https://i.imgur.com/TSGc05L.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    150.00, '230g', '50 x 50 x 10cm', 1),
  ('Caramel Explosion',
   'https://i.imgur.com/TiPDg6K.jpeg',
   array ['https://i.imgur.com/TiPDg6K.jpeg',
    'https://i.imgur.com/R0Gj4py.jpeg',
    'https://i.imgur.com/XEMWiEi.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    200.00, '230g', '50 x 50 x 10cm', 1),
  ('Favna Double Cheese',
   'https://i.imgur.com/xSEKE62.jpeg',
   array ['https://i.imgur.com/xSEKE62.jpeg',
    'https://i.imgur.com/Jo5ubvw.jpeg',
    'https://i.imgur.com/K3xwouF.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    150.00, '230g', '50 x 50 x 10cm', 1),
  ('Choco Passion',
   'https://i.imgur.com/Tm7ELW8.jpeg',
   array ['https://i.imgur.com/Tm7ELW8.jpeg',
    'https://i.imgur.com/Ti6zSwF.jpeg',
    'https://i.imgur.com/gBsz1QR.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    30.00, '230g', '50 x 50 x 10cm', 2),
  ('Sweet Suprise',
   'https://i.imgur.com/koYvwkj.jpeg',
   array ['https://i.imgur.com/koYvwkj.jpeg',
    'https://i.imgur.com/koYvwkj.jpeg',
    'https://i.imgur.com/MUH68rA.jpeg',
    'https://i.imgur.com/P50d5Ae.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    95.00, '230g', '50 x 50 x 10cm', 2),
  ('Lemon Tart',
   'https://i.imgur.com/RWJmZ4g.jpeg',
   array ['https://i.imgur.com/RWJmZ4g.jpeg',
    'https://i.imgur.com/rjts7tf.jpeg',
    'https://i.imgur.com/CGKKdlq.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    100.00, '230g', '50 x 50 x 10cm', 3),
  ('Choclate Tart',
   'https://i.imgur.com/w357wyi.jpeg',
   array ['https://i.imgur.com/EcevOVh.jpeg',
    'https://i.imgur.com/zmR0q5d.jpeg',
    'https://i.imgur.com/w357wyi.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    100.00, '230g', '50 x 50 x 10cm', 3),
  ('Fruit Tart',
   'https://i.imgur.com/h4ijqlU.jpeg',
   array ['https://i.imgur.com/h4ijqlU.jpeg',
    'https://i.imgur.com/6OEQBmP.jpeg',
    'https://i.imgur.com/42dPt9Y.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    50.00, '230g', '50 x 50 x 10cm', 3),
  ('Chocochip Cookie',
   'https://i.imgur.com/IbbaMgw.jpeg',
   array ['https://i.imgur.com/IbbaMgw.jpeg',
    'https://i.imgur.com/UzlbxMy.jpeg',
    'https://i.imgur.com/oT6eNSh.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    30.00, '230g', '50 x 50 x 10cm', 2),
  ('Dariole',
   'https://i.imgur.com/Vxl8CRq.jpeg',
   array ['https://i.imgur.com/Vxl8CRq.jpeg',
    'https://i.imgur.com/ooXN2Ip.jpeg',
    'https://i.imgur.com/sTAPYqj.jpeg',
    'https://i.imgur.com/FfeSid9.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    150.00, '230g', '50 x 50 x 10cm', 1),
  ('Cupcake Basket',
   'https://i.imgur.com/iv1b8Tx.jpeg',
   array ['https://i.imgur.com/iv1b8Tx.jpeg',
    'https://i.imgur.com/Tu2bxm3.jpeg',
    'https://i.imgur.com/mJBbERg.jpeg',
    'https://i.imgur.com/WCbRw8M.jpeg'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    150.00, '230g', '50 x 50 x 10cm', 3),
  ('Cookie',
   'https://i.imgur.com/rsG9yBi.jpeg',
   array ['https://i.imgur.com/rsG9yBi.jpeg',
    'https://i.imgur.com/wiqgv2z.jpeg',
    'https://i.imgur.com/0rKH5x4.jpeg',
    'https://i.imgur.com/2ZAR8ZM.jpeg4'],
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam. Ullamcorper malesuada proin libero nunc consequat. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Massa enim nec dui nunc mattis enim ut tellus elementum. Suscipit tellus mauris a diam maecenas nisi vitae.',
    30.00, '230g', '50 x 50 x 10cm', 2);

insert into
card_font (name, attachments)
values
  ('birthday', 'https://i.imgur.com/PiU106D.jpeg'),
  ('birthday', 'https://i.imgur.com/rCU599P.jpeg'),
  ('mother', 'https://i.imgur.com/ELQpVhQ.jpeg'),
  ('congrat', 'https://i.imgur.com/bfCWXBA.jpeg'),
  ('thanks', 'https://i.imgur.com/K2iCH0Y.jpeg'),
  ('getwell', 'https://i.imgur.com/NEVZbK2.jpeg');

insert into
card_decorations (name, attachments)
values
  ('deco1', 'https://i.imgur.com/2Nia2Ab.png'),
  ('deco2', 'https://i.imgur.com/F0vDRDc.png'),
  ('deco3', 'https://i.imgur.com/UzAyrZw.png'),
  ('deco4', 'https://i.imgur.com/diePPqu.png'),
  ('deco5', 'https://i.imgur.com/qedIBxA.png'),
  ('deco6', 'https://i.imgur.com/CbdchnN.png'),
  ('deco7', 'https://i.imgur.com/SfokdhZ.png'),
  ('deco8', 'https://i.imgur.com/geJCvR7.png'),
  ('deco9', 'https://i.imgur.com/1WsUGOZ.png'),
  ('deco10', 'https://i.imgur.com/hiEnIS2.png'),
  ('deco11', 'https://i.imgur.com/WiWaawv.png'),
  ('deco12', 'https://i.imgur.com/Hvwyrxi.png'),
  ('deco13', 'https://i.imgur.com/5grpnfc.png'),
  ('deco14', 'https://i.imgur.com/i8mT6GO.png'),
  ('deco15', 'https://i.imgur.com/ZeRTZ8A.png'),
  ('deco16', 'https://i.imgur.com/tTXVpC5.png'),
  ('deco17', 'https://i.imgur.com/36A9FuX.png'),
  ('deco18', 'https://i.imgur.com/uwwVElB.png');
