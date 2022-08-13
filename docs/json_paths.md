# Necessary Keys and DataFields for Extraction:

I would need to following keys in the json file: 
Structured in the following sections:

Notes: 
- '[]' signalizes that there are multiple Keys and Elements and all of them shall be considered.
- the current structure '@value' shall not be kept in the final json, it shall be like {'Document.Header.Name': 'Document.Header.Name.@value'}

----

**Necessary Information from Document.Header: (Relevant for all Document.Body.batch.Series.SeriesElements.Elem[])
Document.Header.Name.@value
Document.Header.Kommentar.Text.@value
Document.Header.Ersteller.@value
Document.Header.Modifikator.@value
Document.Header.Terminologie.@value
Document.Header.SeriesName.@value
Document.Header.Erstellung.@value
Document.Header.Modifikation.@value
Document.Header.ProgVersion.@value
Document.Header.LizenzInfo.@value

----

** Parsing the Document.Body.UnitTables: (Relevant for all Document.Body.batch.Series.SeriesElements.Elem[])
Document.Body.UnitTables.Key[].@value
Document.Body.UnitTables.Elem[].Units.Key[].@value
Document.Body.UnitTables.Elem[].Units.Elem[].DisplayName.Text.@value
Document.Body.UnitTables.Elem[].Units.Elem[].DisplayName.ZmsRef.@value
Document.Body.UnitTables.Elem[].Units.Elem[].Name.@value
Document.Body.UnitTables.Elem[].Units.Elem[].Factor.@value
Document.Body.UnitTables.Elem[].Units.Elem[].Sortindex.@value
Document.Body.UnitTables.Elem[].Units.Elem[].Visible.@value
Document.Body.UnitTables.Elem[].Units.Elem[].Deleteable.@value
Document.Body.UnitTables.Elem[].Units.Elem[].Guid.@value

----

** Parsing the Document.Body.batch: (Main Part for Measurement Data)
Document.Body.batch.Guid.@value

Document.Body.batch.EventsDef.EventDefinitions.Key[].@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].NameIntern.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].NameAnzeige.Text.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].NameAnzeige.ZmsRef.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].ID.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].AlternativeID.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].ArtDerIndizierung.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].IndexKanalID.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].Level.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].Visible.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].Version.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].DataSourceDefGroupId.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].Trenner.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].Temporaer.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].ZaehlerNullBasiert.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].Indiziert.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].Flags.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].ManualCreated.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].Guid.@value

Document.Body.batch.SeriesDef.SeriesLevelDefs.Elem[].LevelIndex.@value
Document.Body.batch.SeriesDef.SeriesLevelDefs.Elem[].Evaluation.ErgebnisKurve.Dateiname.@value
Document.Body.batch.SeriesDef.SeriesLevelDefs.Elem[].Evaluation.ErgebnisKurve.X0.@value
Document.Body.batch.SeriesDef.SeriesLevelDefs.Elem[].Evaluation.ErgebnisKurve.Y0.@value
Document.Body.batch.SeriesDef.SeriesLevelDefs.Elem[].Evaluation.ErgebnisKurve.XEinheitenKlasse.@value
Document.Body.batch.SeriesDef.SeriesLevelDefs.Elem[].Evaluation.ErgebnisKurve.YEinheitenKlasse.@value
Document.Body.batch.SeriesDef.SeriesLevelDefs.Elem[].Evaluation.ErgebnisKurve.Dateiname.@value

Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].ID.@value
Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].Typ.@value
Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].SeriesLevel.@value
Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].Name.Text.@value
Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].NameDeco.Text.@value
Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].Kurzzeichen.Text.@value
Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].KurzzeichenDeco.Text.@value
Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].Guid.@value
Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].QS_ParProp.@value
Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].QS_SkalProp.@value
Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].QS_SelProp.@value
Document.Body.batch.SeriesDef.TestTaskDefs.Elem[].DeviceManager.PrivateContext.EigenschaftenListe.Elem[].QS_TextPar.@value (not always available)

Document.Body.batch.Series.Guid.@value 

Document.Body.batch.Series.SeriesElements.Elem[].Guid.@value
Document.Body.batch.Series.SeriesElements.Elem[].CurrentTestTaskIndex.@value
Document.Body.batch.Series.SeriesElements.Elem[].ID.@value
Document.Body.batch.Series.SeriesElements.Elem[].Nummer.@value
Document.Body.batch.Series.SeriesElements.Elem[].Label.@value
Document.Body.batch.Series.SeriesElements.Elem[].Pruefnummer.@value
Document.Body.batch.Series.SeriesElements.Elem[].IstGeprueft.@value
Document.Body.batch.Series.SeriesElements.Elem[].IstExportiert.@value
Document.Body.batch.Series.SeriesElements.Elem[].IstSelektiert.@value
Document.Body.batch.Series.SeriesElements.Elem[].HatAusreisser.@value
Document.Body.batch.Series.SeriesElements.Elem[].Imported.@value


Document.Body.batch.Series.SeriesElements.Elem[].EvalContext.ParamContext.ParameterListe.Elem[].ID.@value
Document.Body.batch.Series.SeriesElements.Elem[].EvalContext.ParamContext.ParameterListe.Elem[].Typ.@value
Document.Body.batch.Series.SeriesElements.Elem[].EvalContext.ParamContext.ParameterListe.Elem[].QS_Par.@value
Document.Body.batch.Series.SeriesElements.Elem[].EvalContext.ParamContext.ParameterListe.Elem[].QS_ValPar.@value


Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.SingleGroupDataBlock.NumberOfLines.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.SingleGroupDataBlock.DataChannels.Elem[].DataArray.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.SingleGroupDataBlock.DataChannels.Elem[].TrsChannelId.@value

Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.TrsChannels.Elem[].KanalID.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.TrsChannels.Elem[].Maximum.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.TrsChannels.Elem[].Messlaenge.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.TrsChannels.Elem[].Gueltig.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.TrsChannels.Elem[].AbsoluteMeasuring.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.TrsChannels.Elem[].AbsoluteMeasuringUsed.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.TrsChannels.Elem[].RawValueInverted.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.TrsChannels.Elem[].bFixedGaugeLengthActive.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.TrsChannels.Elem[].bFixedGaugeLengthValue.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.TrsChannels.Elem[].SensorSerialNumber.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.TrsChannels.Elem[].bFixedGaugeLengthValue.@value

Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.DataSourceEventManager.Elem[].ID.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.DataSourceEventManager.Elem[].Name.Text.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.DataSourceEventManager.Elem[].Name.ZmsRef.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.DataSourceEventManager.Elem[].NameDefinition.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.DataSourceEventManager.Elem[].Zeile.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.DataSourceEventManager.Elem[].tempEreignis.@value
Document.Body.batch.Series.SeriesElements.Elem[].SeriesElements.Elem[].RealTimeCapture.Trs.DataSourceEventManager.Elem[].Index.@value