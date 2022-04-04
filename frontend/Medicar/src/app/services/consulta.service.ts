import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Observable, take } from 'rxjs';
import { Consulta } from 'src/app/models/Consulta';

@Injectable()
export class ConsultaService {

  baseUrl = environment.apiURL + 'consultas/'

  constructor(private http: HttpClient) {

  }

  getConsultas() : Observable<Consulta[]> {
    console.log(this.baseUrl);
    return this.http.get<Consulta[]>(this.baseUrl);
  }

  post(consulta: Consulta): Observable<Consulta> {
    return this.http
      .post<Consulta>(this.baseUrl, consulta)
      .pipe(take(1));
  }

  deleteConsulta(id: number): Observable<any> {
    return this.http
      .delete(`${this.baseUrl}${id}`)
      .pipe(take(1));
  }
}
