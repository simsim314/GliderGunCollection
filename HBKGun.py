import golly as g 
import json 
import os
'''
adjustablePart1Str = "8$24b2o$23bobo$17b2o4bo$15bo2bo2b2ob4o$15b2obobobobo2bo$18bobobobo$18bobob2o$19bo2$32b2o$23b2o7bo$23b2o5bobo$30b2o7$20b2o$21bo$18b3o$18bo8$51b2o$51bo$53bo$33b2o14b5o$34bo13bo$34bobo12b3o$35b2o15bo$49b4o$44b2o3bo3b2o$44b2o4b3o2bo$52bob2o$52bo$51b2o3$43b2o$43bo$44b3o$46bo!"
adjustablePart1 = g.parse(adjustablePart1Str, 2410, 520)

adjustablePart2Str = "4$14b2o$13bobo$7b2o4bo$5bo2bo2b2ob4o$5b2obobobobo2bo$8bobobobo$8bobob2o$9bo2$22b2o$13b2o7bo$13b2o5bobo$20b2o7$10b2o$11bo$8b3o$8bo24b2o$33bo$35bo$15b2o14b5o$16bo13bo$16bobo12b3o$17b2o15bo$31b4o$26b2o3bo3b2o$26b2o4b3o2bo$34bob2o$34bo$33b2o3$25b2o$25bo$26b3o$28bo!"
adjustablePart2 = g.parse(adjustablePart2Str, 80, 230)

gunPart1Str = "1157b2o$1156bobo$1150b2o4bo$1148bo2bo2b2ob4o$1148b2obobobobo2bo$1151bobobobo$1151bobob2o$1152bo2$1165b2o$1156b2o7bo$137b2o1017b2o5bobo$136bobo1024b2o$130b2o4bo$128bo2bo2b2ob4o$128b2obobobobo2bo$131bobobobo$131bobob2o$132bo$1153b2o$145b2o1007bo$136b2o7bo1005b3o$136b2o5bobo1005bo$143b2o7$133b2o1049b2o$134bo1049bo$131b3o1052bo$131bo1034b2o14b5o$1167bo13bo$1167bobo12b3o$1168b2o15bo$1182b4o$1177b2o3bo3b2o$1177b2o4b3o2bo$1185bob2o$1185bo$1184b2o3$1176b2o$1176bo$1177b3o$1179bo61$31bo$31b3o$34bo$33b2o$48b2o$48bo$46bobo$35bo10b2o$34bobo$34bobo$29b2o4bo$28bobo15b2o$28bo17bobo$20b2o5b2o19bo$21bo26b2o$21bobo$22b2o4$37b2o$37b2o9$49b2o$49bo$47bobo$47b2o2$87b2o$4bo82b2o5b2o$2b5o14b2o71b2o$bo5bo13bo39bo$bo2b3o12bobo29b2o6b3o$2obo15b2o30bo6bo14b2o17b2o$o2b4o42bobo6b2o14bo17b2o$b2o3bo3b2o37b2o23bobo21b2o$3b3o4b2o63b2o21b2o$3bo$2obo32b2o$2ob2o30bobo$35bo25b2o$34b2o25b2o$11b2o17bo$12bo17b3o$9b3o21bo$9bo22b2o2$54b2o$54bo47bo$48bo6b3o42b3o$47bobo7bo10b2o29bo$48bo18bobo29b2o$42b2o23bo$35b2o5bobo21b2o204b2o$35b2o7bo226bobo$44b2o219b2o4bo$263bo2bo2b2ob4o$31bo49b2o180b2obobobobo2bo$30bobob2o46bo183bobobobo$30bobobobo45bobo181bobob2o$29b2obobobo2bo43b2o182bo$30bo2b2ob4o$30bo4bo244b2o$31b3obo2b2o60b2o169b2o7bo$33b2o3b2o43b2o15b2o169b2o5bobo$82bobo193b2o$82bo$81b2o4$100b2o$101bo166b2o$101bobo165bo$102b2o162b3o$266bo3$83bob2o$83b2obo2$92b2o$92b2o5$104b2o$104bo$102bobo$102b2o6$82bo$82b3o$85bo$84b2o7$79b2o$80bo$80bobo$81b2o3$95b2o$95bobo$97bo$97b2o3$77bob2o$77b2obo$105b2o$86b2o17bo$86b2o15bobo$103b2o10$184bo$184b3o$187bo$186b2o$96b2o103b2o$96bo104bo$94bobo11b2o89bobo$94b2o12bo79bo10b2o$106bobo78bobo$102b2o2b2o79bobo$102b2o78b2o4bo$181bobo15b2o$181bo17bobo$173b2o5b2o19bo$101b2o71bo26b2o$101b2o4b2o65bobo$107b2o66b2o4$190b2o$190b2o$106b2o$106bobo$108bo$108b2o5$202b2o$202bo$200bobo$200b2o2$240b2o$157bo82b2o5b2o$155b5o14b2o71b2o$154bo5bo13bo39bo$154bo2b3o12bobo29b2o6b3o$153b2obo15b2o30bo6bo14b2o17b2o$153bo2b4o42bobo6b2o14bo17b2o$154b2o3bo3b2o37b2o23bobo21b2o$156b3o4b2o63b2o21b2o$156bo$153b2obo32b2o664bo$153b2ob2o30bobo664b3o$188bo25b2o642bo$187b2o25b2o641b2o$164b2o17bo$165bo17b3o$162b3o21bo662b2o$162bo22b2o662bo$846b2obo$207b2o637bo2b3o4b2o$207bo47bo591b2o3bo3b2o$201bo6b3o42b3o593b4o$200bobo7bo10b2o29bo596bo15b2o$201bo18bobo29b2o596b3o12bobo$195b2o23bo632bo13bo$188b2o5bobo21b2o627b5o14b2o$188b2o7bo650bo$197b2o651bo26bo$849b2o24b3o$184bo49b2o638bo$183bobob2o46bo638b2o$183bobobobo45bobo621b2o$182b2obobobo2bo43b2o622bo$183bo2b2ob4o667bobo$183bo4bo672b2o10bo$184b3obo2b2o60b2o617bobo$186b2o3b2o43b2o15b2o617bobo$235bobo635bo4b2o$235bo625b2o15bobo$234b2o624bobo17bo$860bo19b2o$859b2o2$253b2o$254bo$254bobo$255b2o$870b2o$870b2o2$236bob2o$236b2obo2$245b2o$245b2o3$858b2o$859bo$257b2o165b2o433bobo$257bo165bobo396bo37b2o$255bobo159b2o4bo338b2o56b3o81b2o$255b2o158bo2bo2b2ob4o334bo56bo84bo$415b2obobobobo2bo304b2o26bobo56b2o85bo$418bobobobo180b2o4bo121bo26b2o12b2o110b2o14b5o$418bobob2o172b2o7bobo2bobo104bo15bobo38bo24b2o48b2o36bo13bo$419bo177bo9b4o2bo43b2o56b3o16b2o39b3o6b2o13bo49bo6b2o29bobo12b3o$597bobo6bo4bobo43bo56bo62bo6b2o11bobo50bo6bo30b2o15bo$235bo196b2o164b2o6b2o2b2ob2o12b2o26bobo56b2o81b2o50b2o6bobo42b4o$235b3o185b2o7bo183bo11bo26b2o12b2o187b2o37b2o3bo3b2o$238bo184b2o5bobo177b2ob4o2bo8bobo38bo24b2o201b2o4b3o2bo$237b2o191b2o143b2o33b2obo3b3o9b2o39b3o6b2o13bo210bob2o$576bo39bo55bo6b2o11bobo176b2o32bo$576bobo37b2o74b2o177bobo30b2o$577b2o187b2o78b2o25bo$766b2o78b2o25b2o$878bo17b2o$876b3o17bo$232b2o186b2o453bo21b3o$233bo187bo239b2o212b2o22bo$233bobo182b3o240b2o$234b2o182bo316b2o32b2o82b2o$735b2o11b2o20bo83bo$557bo190bo20bo13b2o3b2o14b2o45b3o6bo$248b2o306bobo190b3o17b2o13bo3bo15bo5b2o39bo7bobo$248bobo305bobo192bo29b3o5b3o13b3obobo48bo$250bo306bo72b2o32b2o115bo9bo15bobo7b2o46b2o$250b2o378b2o11b2o20bo142b2o7b2o45bobo5b2o$643bo20bo13b2o3b2o14b2o163bo7b2o$578b2o24b2o38b3o17b2o13bo3bo15bo5b2o156b2o$230bob2o344b2o11b2o10bobo4b2o34bo29b3o5b3o13b3obobo$230b2obo357bo11bo6bo65bo9bo15bobo7b2o163bo$258b2o332b3o7b2o7b3o89b2o7b2o159b2obobo$239b2o17bo335bo18bo258bobobobo$239b2o15bobo610bo2bobobobob2o$256b2o611b4ob2o2bo2bo$873bo4b2o$871bobo$871b2o11$249b2o$249bo$247bobo11b2o$247b2o12bo$259bobo$255b2o2b2o$255b2o4$254b2o$254b2o4b2o$260b2o3$894bo$892b3o$891bo$259b2o630b2o$259bobo$261bo84bo$261b2o83b3o550b2o$349bo550bo$348b2o550bob2o$363b2o527b2o4b3o2bo$363bo528b2o3bo3b2o$361bobo533b4o$350bo10b2o520b2o15bo$349bobo530bobo12b3o$349bobo530bo13bo$344b2o4bo530b2o14b5o$343bobo15b2o437bo100bo$343bo17bobo434b3o98bo$335b2o5b2o19bo433bo101b2o$336bo26b2o432b2o$336bobo$337b2o$805b2o$806bo$806bob2o$352b2o444b2o4b3o2bo$352b2o444b2o3bo3b2o$803b4o$789b2o15bo$788bobo12b3o$788bo13bo$787b2o14b5o$807bo$707bo97bo$705b3o97b2o$364b2o288bo49bo$364bo287b3o49b2o$362bobo286bo$362b2o287b2o$712b2o$402b2o309bo$319bo82b2o5b2o248b2o52bob2o$317b5o14b2o71b2o249bo44b2o4b3o2bo$316bo5bo13bo39bo283bob2o41b2o3bo3b2o$316bo2b3o12bobo29b2o6b3o275b2o4b3o2bo46b4o$315b2obo15b2o30bo6bo14b2o17b2o243b2o3bo3b2o33b2o15bo$315bo2b4o42bobo6b2o14bo17b2o248b4o34bobo12b3o$316b2o3bo3b2o37b2o23bobo21b2o228b2o15bo34bo13bo$318b3o4b2o63b2o21b2o227bobo12b3o34b2o14b5o$318bo323bo13bo57bo$315b2obo32b2o288b2o14b5o50bo$315b2ob2o30bobo308bo50b2o$350bo25b2o281bo$349b2o25b2o281b2o$326b2o17bo$327bo17b3o$324b3o21bo$324bo22b2o2$369b2o$369bo47bo$363bo6b3o42b3o$362bobo7bo10b2o29bo$363bo18bobo29b2o$357b2o23bo$350b2o5bobo21b2o$350b2o7bo$359b2o2$346bo49b2o$345bobob2o46bo$345bobobobo45bobo$344b2obobobo2bo43b2o$345bo2b2ob4o$345bo4bo$346b3obo2b2o60b2o$348b2o3b2o43b2o15b2o$397bobo$397bo$396b2o$607bo$607b3o$610bo$415b2o192b2o$416bo$416bobo$417b2o4$398bob2o217b2o$398b2obo210b2o5bobo$612b2o7bo$407b2o212b2o$407b2o$608bo$607bobob2o$607bobobobo$604b2obobobobo2bo$419b2o183bo2bo2b2ob4o$419bo186b2o4bo$417bobo192bobo$417b2o194b2o6$397bo$397b3o176b2o$400bo174bobo$399b2o168b2o4bo$567bo2bo2b2ob4o$567b2obobobobo2bo$570bobobobo$570bobob2o$571bo$621bo$394b2o188b2o35b3o$395bo179b2o7bo39bo$395bobo177b2o5bobo38b2o$396b2o184b2o3$410b2o$410bobo$412bo$412b2o219b2o$572b2o52b2o5bobo$573bo52b2o7bo$392bob2o174b3o62b2o$392b2obo174bo$420b2o200bo$401b2o17bo200bobob2o$401b2o15bobo200bobobobo$418b2o198b2obobobobo2bo$618bo2bo2b2ob4o$620b2o4bo$626bobo$627b2o10$411b2o$411bo$409bobo11b2o$409b2o12bo$421bobo$417b2o2b2o$417b2o4$416b2o$416b2o4b2o$422b2o5$648bo$421b2o225b3o$421bobo227bo$423bo226b2o$423b2o2$505bo$505b3o$508bo$507b2o$522b2o136b2o$522bo130b2o5bobo$520bobo130b2o7bo$509bo10b2o140b2o$508bobo$508bobo138bo$503b2o4bo138bobob2o$502bobo15b2o126bobobobo$502bo17bobo122b2obobobobo2bo$494b2o5b2o19bo122bo2bo2b2ob4o$495bo26b2o123b2o4bo$495bobo155bobo$496b2o156b2o4$511b2o$511b2o9$523b2o$523bo$521bobo$521b2o2$561b2o$478bo82b2o5b2o$476b5o14b2o71b2o$475bo5bo13bo39bo$475bo2b3o12bobo29b2o6b3o$474b2obo15b2o30bo6bo14b2o17b2o$474bo2b4o42bobo6b2o14bo17b2o$475b2o3bo3b2o37b2o23bobo21b2o$477b3o4b2o63b2o21b2o$477bo198bo$474b2obo32b2o164b3o$474b2ob2o30bobo167bo$509bo25b2o141b2o$508b2o25b2o$485b2o17bo$486bo17b3o$483b3o21bo$483bo22b2o2$528b2o158b2o$528bo47bo104b2o5bobo$522bo6b3o42b3o104b2o7bo$521bobo7bo10b2o29bo116b2o$522bo18bobo29b2o$516b2o23bo135bo$509b2o5bobo21b2o134bobob2o$509b2o7bo157bobobobo$518b2o153b2obobobobo2bo$673bo2bo2b2ob4o$505bo49b2o118b2o4bo$504bobob2o46bo124bobo$504bobobobo45bobo123b2o$503b2obobobo2bo43b2o$504bo2b2ob4o$504bo4bo$505b3obo2b2o60b2o$507b2o3b2o43b2o15b2o$556bobo$556bo$555b2o4$574b2o$575bo$575bobo$576b2o4$557bob2o$557b2obo2$566b2o$566b2o5$578b2o$578bo$576bobo$576b2o6$556bo556b3o$559bo$558b2o7$553b2o$554bo$554bobo$555b2o3$569b2o$569bobo$571bo$571b2o3$551bob2o$551b2obo$579b2o$560b2o17bo$560b2o15bobo$577b2o14$570b2o$570bo$568bobo11b2o$568b2o12bo$580bobo$576b2o2b2o$576b2o4$575b2o$575b2o4b2o$581b2o6$580b2o$580bobo$582bo$582b2o!"
gunPart1 = g.parse(gunPart1Str, 1277,539)

gunPart2Str = "529b2o$530bo$530bobo$531b2o6$530b2o$530b2o4b2o$536b2o4$535b2o$531b2o2b2o$530bobo$530bo12b2o$529b2o11bobo$542bo$541b2o14$534b2o$533bobo15b2o$533bo17b2o$532b2o$558bob2o$558b2obo3$540b2o$541bo$541bobo$542b2o3$556b2o$556bobo$558bo$558b2o7$553b2o$553bo$554b3o$556bo6$535b2o$534bobo$534bo$533b2o5$545b2o$545b2o2$552bob2o$552b2obo4$535b2o$535bobo$537bo$537b2o4$556b2o$556bo$554bobo$537b2o15b2o43b2o3b2o$537b2o60b2o2bob3o$603bo4bo$599b4ob2o2bo$554b2o43bo2bobobob2o$429b2o123bobo45bobobobo$429bobo124bo46b2obobo$431bo4b2o118b2o49bo$427b4ob2o2bo2bo$427bo2bobobobob2o153b2o$430bobobobo157bo7b2o$431b2obobo134b2o21bobo5b2o$435bo135bo23b2o$538b2o29bobo18bo$421b2o116bo29b2o10bo7bobo$422bo7b2o104b3o42b3o6bo$422bobo5b2o104bo47bo$423b2o158b2o2$605b2o22bo$605bo21b3o$606b3o17bo$608bo17b2o$576b2o25b2o$433b2o141b2o25bo$433bo167bobo30b2ob2o$434b3o164b2o32bob2o$436bo198bo$539b2o21b2o63b2o4b3o$539b2o21bobo23b2o37b2o3bo3b2o$545b2o17bo14b2o6bobo42b4o2bo$545b2o17b2o14bo6bo30b2o15bob2o$577b3o6b2o29bobo12b3o2bo$577bo39bo13bo5bo$543b2o71b2o14b5o$543b2o5b2o82bo$550b2o2$590b2o$589bobo$589bo$588b2o9$600b2o$600b2o4$457b2o156b2o$457bobo155bobo$459bo4b2o123b2o26bo$455b4ob2o2bo2bo122bo19b2o5b2o$455bo2bobobobob2o122bobo17bo$458bobobobo126b2o15bobo$459b2obobo138bo4b2o$463bo138bobo$602bobo$449b2o140b2o10bo$450bo7b2o130bobo$450bobo5b2o130bo$451b2o136b2o$604b2o$604bo$605b3o$607bo2$688b2o$461b2o226bo$461bo227bobo$462b3o225b2o$464bo5$689b2o$689b2o4b2o$695b2o4$694b2o$690b2o2b2o$689bobo$689bo12b2o$688b2o11bobo$701bo$700b2o10$484b2o$484bobo$486bo4b2o$482b4ob2o2bo2bo$482bo2bobobobob2o198b2o$485bobobobo200bobo15b2o$486b2obobo200bo17b2o$490bo200b2o$542bo174bob2o$476b2o62b3o174b2obo$477bo7b2o52bo$477bobo5b2o52b2o$478b2o219b2o$700bo$700bobo$701b2o3$529b2o184b2o$488b2o38bobo5b2o177bobo$488bo39bo7b2o179bo$489b3o35b2o188b2o$491bo$541bo$537b2obobo$536bobobobo$533bo2bobobobob2o$533b4ob2o2bo2bo$537bo4b2o168b2o$535bobo174bo$535b2o176b3o$715bo2$494b2o$494bobo$496bo4b2o$492b4ob2o2bo2bo$492bo2bobobobob2o189b2o$495bobobobo191bobo$496b2obobo191bo$500bo191b2o2$486b2o$487bo7b2o$487bobo5b2o$488b2o214b2o$704b2o2$711bob2o$711b2obo3$498b2o$498bo195b2o$499b3o192bobo$501bo194bo$696b2o4$715b2o$715bo$713bobo$696b2o15b2o43b2o3b2o$696b2o60b2o2bob3o$762bo4bo$758b4ob2o2bo$713b2o43bo2bobobob2o$713bobo45bobobobo$715bo46b2obobo$715b2o49bo2$752b2o$753bo7b2o$730b2o21bobo5b2o$730bo23b2o$697b2o29bobo18bo$698bo29b2o10bo7bobo$695b3o42b3o6bo$695bo47bo$742b2o2$448b2o314b2o22bo$449bo314bo21b3o$447bo317b3o17bo$447b5o14b2o299bo17b2o$452bo13bo268b2o25b2o$449b3o12bobo268b2o25bo$399b2o47bo15b2o294bobo30b2ob2o$400bo47b4o308b2o32bob2o$398bo47b2o3bo3b2o337bo$398b5o14b2o26bo2b3o4b2o241b2o21b2o63b2o4b3o$403bo13bo27b2obo249b2o21bobo23b2o37b2o3bo3b2o$400b3o12bobo30bo255b2o17bo14b2o6bobo42b4o2bo$399bo15b2o31b2o254b2o17b2o14bo6bo30b2o15bob2o$399b4o333b3o6b2o29bobo12b3o2bo$397b2o3bo3b2o328bo39bo13bo5bo$396bo2b3o4b2o48b2o244b2o71b2o14b5o$396b2obo57bo244b2o5b2o82bo$399bo54b3o252b2o$399b2o53bo$749b2o$748bobo$407b2o339bo$408bo338b2o$306b2o97b3o$307bo97bo$305bo$305b5o14b2o$310bo13bo$307b3o12bobo$306bo15b2o$43b2o261b4o$9bo34bo259b2o3bo3b2o444b2o$9b3o30bo260bo2b3o4b2o444b2o$12bo29b5o14b2o240b2obo$11b2o34bo13bo244bo$44b3o12bobo244b2o$43bo15b2o713b2o$3b2o38b4o727bobo$3bo37b2o3bo3b2o262b2o432b2o26bo$2obo36bo2b3o4b2o160b2o101bo433bo19b2o5b2o$o2b3o4b2o28b2obo169bo98b3o434bobo17bo$b2o3bo3b2o31bo167bo100bo437b2o15bobo$3b4o36b2o166b5o14b2o530bo4b2o$3bo15b2o195bo13bo530bobo$4b3o12bobo191b3o12bobo530bobo$7bo13bo29b2o159bo15b2o520b2o10bo$2b5o14b2o29bo159b4o533bobo$2bo46b3o158b2o3bo3b2o528bo$4bo44bo159bo2b3o4b2o527b2o$3b2o204b2obo550b2o$212bo550bo$212b2o550b3o83b2o$766bo84bo$851bobo$220b2o630b2o$221bo$218b3o$218bo3$851b2o$851b2o4b2o$857b2o4$856b2o$852b2o2b2o$851bobo$851bo12b2o$850b2o11bobo$863bo$862b2o11$240b2o$239bobo$233b2o4bo$231bo2bo2b2ob4o611b2o$231b2obobobobo2bo610bobo15b2o$234bobobobo258bo18bo335bo17b2o$234bobob2o159b2o7b2o89b3o7b2o7b3o332b2o$235bo163b2o7bobo15bo9bo65bo6bo11bo357bob2o$406bobob3o13b3o5b3o29bo34b2o4bobo10b2o11b2o344b2obo$248b2o156b2o5bo15bo3bo13b2o17b3o38b2o24b2o$239b2o7bo163b2o14b2o3b2o13bo20bo$239b2o5bobo45b2o7b2o142bo20b2o11b2o378b2o$246b2o46b2o7bobo15bo9bo115b2o32b2o72bo306bo$252bo48bobob3o13b3o5b3o29bo192bobo305bobo$251bobo7bo39b2o5bo15bo3bo13b2o17b3o190bobo306b2o$252bo6b3o45b2o14b2o3b2o13bo20bo190bo$258bo83bo20b2o11b2o$258b2o82b2o32b2o316bo182b2o$450b2o240b3o182bobo$213bo22b2o212b2o239bo187bo$213b3o21bo453b2o186b2o$216bo17b3o$215b2o17bo$238b2o25b2o78b2o$239bo25b2o78b2o187b2o$207b2o30bobo177b2o74b2o37bobo$207bo32b2o176bobo11b2o6bo55bo39bo$204b2obo210bo13b2o6b3o39b2o9b3o3bob2o33b2o143b2o191b2o$204bo2b3o4b2o201b2o24bo38bobo8bo2b4ob2o177bobo5b2o184bo$205b2o3bo3b2o37b2o187b2o12b2o26bo11bo183bo7b2o185b3o$207b4o42bobo6b2o50b2o81b2o56bobo26b2o12b2ob2o2b2o6b2o164b2o196bo$207bo15b2o30bo6bo50bobo11b2o6bo62bo56bo43bobo4bo6bobo$208b3o12bobo29b2o6bo49bo13b2o6b3o39b2o16b3o56b2o43bo2b4o9bo177bo$211bo13bo36b2o48b2o24bo38bobo15bo104bobo2bobo7b2o172b2obobo$206b5o14b2o110b2o12b2o26bo121bo4b2o180bobobobo$206bo85b2o56bobo26b2o304bo2bobobobob2o$208bo84bo56bo334b4ob2o2bo2bo158b2o$207b2o81b3o56b2o338bo4b2o159bobo$251b2o37bo396bobo165bo$251bobo433b2o165b2o$253bo$253b2o3$866b2o$866b2o2$873bob2o$873b2obo2$241b2o$241b2o$856b2o$856bobo$858bo$858b2o2$252b2o$231b2o19bo$232bo17bobo624b2o$232bobo15b2o625bo$233b2o4bo635bobo$238bobo617b2o15b2o43b2o3b2o$238bobo617b2o60b2o2bob3o$239bo10b2o672bo4bo$250bobo667b4ob2o2bo$252bo622b2o43bo2bobobob2o$252b2o621bobo45bobobobo$237b2o638bo46b2obobo$238bo638b2o49bo$235b3o$235bo678b2o$915bo7b2o$892b2o21bobo5b2o$892bo23b2o$859b2o29bobo18bo$860bo29b2o10bo7bobo$857b3o42b3o6bo$857bo47bo$904b2o2$189bo736b2o22bo$189b3o734bo21b3o$192bo734b3o17bo$191b2o736bo17b2o$897b2o25b2o$897b2o25bo$922bobo30b2ob2o$922b2o32bob2o$956bo$282b2o576b2o21b2o63b2o4b3o$201b2o79bo577b2o21bobo23b2o37b2o3bo3b2o$194b2o5bobo80bo581b2o17bo14b2o6bobo42b4o2bo$194b2o7bo60b2o14b5o581b2o17b2o14bo6bo30b2o15bob2o$203b2o60bo13bo618b3o6b2o29bobo12b3o2bo$265bobo12b3o615bo39bo13bo5bo$190bo75b2o15bo580b2o71b2o14b5o$189bobob2o85b4o580b2o5b2o82bo$189bobobobo79b2o3bo3b2o585b2o$186b2obobobobo2bo76b2o4b3o2bo$186bo2bo2b2ob4o84bob2o624b2o$188b2o4bo88bo626bobo$194bobo85b2o626bo$195b2o712b2o2$274b2o$274bo$275b3o$277bo4$921b2o$921b2o2$996b2o$997bo$936b2o59bobo$936bobo59b2o$910b2o26bo$911bo19b2o5b2o$911bobo17bo$912b2o15bobo$924bo4b2o$923bobo71b2o$923bobo71b2o4b2o$912b2o10bo78b2o$911bobo$911bo$910b2o$925b2o75b2o$925bo72b2o2b2o$926b3o68bobo$928bo68bo12b2o$996b2o11bobo$1009bo$1008b2o13$212bo$210b3o788b2o$209bo790bobo15b2o$209b2o789bo17b2o$999b2o$1025bob2o$1025b2obo3$1007b2o$199b2o807bo$198bobo5b2o800bobo$198bo7b2o801b2o$197b2o2$211bo811b2o$207b2obobo810bobo$206bobobobo812bo$203bo2bobobobob2o809b2o$203b4ob2o2bo2bo$207bo4b2o$205bobo$205b2o3$1020b2o$1020bo$1021b3o$1023bo6$1002b2o$1001bobo$1001bo$1000b2o5$846bo165b2o$844b3o165b2o$843bo$843b2o174bob2o$1019b2obo4$1002b2o$1002bobo$833b2o169bo$832bobo5b2o162b2o$832bo7b2o$831b2o2$845bo177b2o$841b2obobo176bo$840bobobobo174bobo$837bo2bobobobob2o154b2o15b2o43b2o3b2o$837b4ob2o2bo2bo154b2o60b2o2bob3o$841bo4b2o222bo4bo$839bobo224b4ob2o2bo$839b2o180b2o43bo2bobobob2o$1021bobo45bobobobo$1023bo46b2obobo$1023b2o49bo2$1060b2o$1061bo7b2o$1038b2o21bobo5b2o$1038bo23b2o$1005b2o29bobo18bo$1006bo29b2o10bo7bobo$1003b3o42b3o6bo$1003bo47bo$1050b2o2$1072b2o22bo$1072bo21b3o$1073b3o17bo$1075bo17b2o$1043b2o25b2o$1043b2o25bo$1068bobo30b2ob2o$1068b2o32bob2o$1102bo$1006b2o21b2o63b2o4b3o$1006b2o21bobo23b2o37b2o3bo3b2o$1012b2o17bo14b2o6bobo42b4o2bo$1012b2o17b2o14bo6bo30b2o15bob2o$1044b3o6b2o29bobo12b3o2bo$1044bo39bo13bo5bo$1010b2o71b2o14b5o$1010b2o5b2o82bo$1017b2o2$1057b2o$1056bobo$1056bo$1055b2o9$1067b2o$1067b2o4$1082b2o$1082bobo$1056b2o26bo$1057bo19b2o5b2o$1057bobo17bo$1058b2o15bobo$1070bo4b2o$1069bobo$1069bobo$1058b2o10bo$1057bobo$1057bo$1056b2o$1071b2o$1071bo$1072b3o$1074bo69$981bo$979b3o$978bo$978b2o7$968b2o$967bobo5b2o$967bo7b2o$966b2o2$980bo$976b2obobo$975bobobobo$972bo2bobobobob2o$972b4ob2o2bo2bo$976bo4b2o$974bobo$974b2o!"
gunPart2 = g.parse(gunPart2Str)


p0 = 2656
d = 0#19909668
dist = 0#60000

gld1 = g.parse("bo$o$3o!", 17, 316)
gld2 = g.parse("bo$o$3o!", 2425, 542)

#g.putcells(adjustablePart1, dist + d, dist -d)
g.putcells(gunPart1, dist, dist)

#g.putcells(gunPart2)
#g.putcells(adjustablePart2, d,  -d)

#g.putcells(gld1)
g.putcells(gld2, -10, 10)

g.exit()
'''
gun = []
gunRef = g.evolve(g.transform(gun, 1, 1, -1, 0, 0, 1), 3)
Define = "SYNTH"#"GUN"

def SLToListXY(cells):
	list = []
	
	for i in xrange(0, len(cells), 2):
		list.append((cells[i], cells[i + 1]))

	list.sort(key=lambda tup: 1000000 * tup[1] + tup[0])
	
	x0, y0 = list[0]
	return [(x - x0, y - y0) for x, y in list]

	
def IsSL(x, y, slXY):
	for xi, yi in slXY:
		if g.getcell(x + xi, y + yi) != 1:
			return False
			
	return True

def DeleteSL(x, y, slXY):
	for xi, yi in slXY:
		g.setcell(x + xi, y + yi, 0)
		
def PutSL(x, y, slXY):
	for xi, yi in slXY:
		g.setcell(x + xi, y + yi, 1)


def PutData(data, recog):			
	for x, y, i in data:
		PutSL(x, y, recog[i])
		
#0 - HB
#1 - block
#2 - ship 
#3 - wide beehive
#4 - boat 
#5 - rotated boat
#6-9 - NW glider
#10-13 - NE gliders
#14 - blinker
#15 - beehive standing
#16 - boat

recGolly = [g.parse("4b2o$3bo2bo$3bobo$b2obo$o2bo$obo$bo!"), g.parse("2o$2o"), g.parse("2o$obo$b2o!"), g.parse("b2o$o2bo$b2o!"), g.parse("bo$obo$2o!"), g.parse("bo$obo$b2o!")]

for i in xrange (0, 4):
	recGolly.append(g.evolve(g.parse("2o$b2o$o!"), i))

for i in xrange (0, 4):
	recGolly.append(g.evolve(g.parse("3o$o$bo!"), i))

recGolly.append(g.parse("3o!"))
recGolly.append(g.parse("bo$obo$obo$bo!"))
recGolly.append(g.parse("b2o$obo$bo!"))

recog = [SLToListXY(c) for c in recGolly]


def ReadNext(data, recog):
	rect = g.getrect()
	
	if rect == []:
		return False
		
	d = g.getcells([rect[0], rect[1], rect[2], 1])
	
	x0 = d[0]
	y0 = d[1]
	
	found = False
	
	for i in xrange(0, len(recog)):
		r = recog[i]
		
		if IsSL(x0, y0, r):
			
			DeleteSL(x0, y0, r)
			data.append((x0, y0, i))
			found = True
			break
	
	return found

def ReadData(recog):
	data = []
	
	if os.path.exists('hbkR.data'):
		with open('hbkR.data', 'r') as f:
			return json.load(f)

	while ReadNext(data, recog):
		i = 1
	
	with open('hbkR.data', 'wb') as f:
		json.dump(data, f)
		
	return data

	
recipes = []

#recipes.append([(5, 7, 13), (-4, 11, 9), (-11, 17, 8), (-5, 17, 7), (15, 22, 11)])
recipes.append([(-4, 5, 6), (10, 7, 13), (-5, 13, 8), (11, 20, 10)])
recipes.append([(2, 2, 12), (-4, 5, 9)])
recipes.append([(2, 2, 12), (-2, 3, 6), (7, 5, 10)])
recipes.append([(-1, 1, 9), (2, 4, 12)])
recipes.append([(5, 0, 10), (-3, 4, 6), (-9, 6, 9)])
recipes.append([(-9, -2, 7), (0, 2, 13), (10, 8, 12)])

for i in xrange(0, 8):
	recipes.append(recog[i + 7])

recipes.append([(5, 4, 13), (0, 6, 8)])
recipes.append([(2, -4, 13), (1, 0, 9), (6, 5, 12)])
recipes.append([(6, 1, 10), (-2, 5, 6), (-8, 7, 7)])

DgunR = 0
DgunL = 0
DLGunXY = [(0,0), (0,0), (-1,1), (-1,1)]
DRGunXY = [(0,0), (-1,1), (0,1), (0,1)]
GunDelta = 6000

def PutGun(idx, x0, y0):
	global DgunR
	global DgunL
	global gun
	global gunRef
	
	if idx > 9:
		dx, dy = DRGunXY[idx - 10]
		gun = g.evolve(gun, GunDelta * 4)
		
		g.putcells(g.evolve(gun, idx - 10), x0 + DgunR + dx, y0 + DgunR + dy)
		DgunR += GunDelta
	else:
		dx, dy = DLGunXY[idx - 6]
		gunRef = g.evolve(gunRef, GunDelta * 4)
		g.putcells(g.evolve(gunRef, idx - 6), x0 -DgunL + dx, y0 +DgunL + dy)
		DgunL += GunDelta
		
def PlaceRecipe(idx, x0, y0, d):
	global recipes
	global recog
	
	for x, y, i in recipes[idx]:
		if i > 9:
			if Define == "SYNTH":
				PutSL(x + x0 + d, y + y0 + d, recog[i])
			else:
				PutGun(i, x + x0 + d, y + y0 + d)	
		else:
			if Define == "SYNTH":
				PutSL(x + x0 - d, y + y0 + d, recog[i])
			else:
				PutGun(i, x + x0 - d, y + y0 + d)	


def PlaceData(data, d0):
	global recipes
	global recog
	
	d = d0 
	cnt = 0 
	
	for x, y, i in data:
		if i >= 6 and i <= 13:
			continue 
			
		PlaceRecipe(i, x, y, d)
		d += 25
		
		cnt += 1
		
		if (Define == "SYNTH" and cnt % 100 == 0) or Define == "GUN":
			g.show(str(cnt) +" / " + str(len(data)))
			g.update()
			
	d += 1000
	
	for x, y, i in data:
		if not(i >= 6 and i <= 13):
			continue 
		
		if i > 9:
			if Define == "SYNTH":
				PutSL(x + d, y + d,  recog[i])
			else:
				PutGun(i, x + d, y + d)	
			
		else:
			if Define == "SYNTH":
				PutSL(x - d, y + d,  recog[i])
			else:
				PutGun(i, x - d, y + d)	
			

#PlaceRecipe(0, 0, 0, 100000)
			
data = ReadData(recog)

#data.sort(key=lambda tup: 10000000 * (tup[1] + tup[0]) + tup[1])
	
#g.putcells(gun)
#g.putcells(g.evolve(gun, 2200 * 4), 2200, 2200)
#
#PlaceData(data, 100000) 

#if Define == "SYNTH":
PlaceData(data, 0)
#PlaceData(data, 25000000)
#else:
#	PlaceData(data, 100000) 

#PutData(data, recog)

#for i in xrange


	
#PutSL(0,0,recog[14])
	
#g.show(str(len(data)))
#g.setclipstr(str(ReadData(recog)))
#g.show(str((ReadData(recog))))
#PutData(ReadData(recog), recog)
